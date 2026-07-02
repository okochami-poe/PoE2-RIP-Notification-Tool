import json
import os
import re
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk
from io import BytesIO
import requests

# 新しい機能（スクショ・ウィンドウ指定）のためのライブラリ
import pygetwindow as gw
from PIL import ImageGrab

CONFIG_FILE = "config.json"

TEXTS = {
    "title": "PoE2 死亡通知ツール v2",
    "webhook": "Discord ウェブフック URL:",
    "logpath": "PoE2 Client.txt のパス:",
    "platform": "ゲームの種類 (Platform):",
    "lang_lbl": "PoE2のゲーム内言語設定:",
    "send_ss_lbl": "死亡時にスクリーンショットも送信する",
    "test_btn": "🔗 Webhook テスト送信",
    "save_btn": "設定を保存",
    "save_success": "設定を保存しました。",
    "err_input": "Webhook URLとログのパスを入力してください。",
    "err_nofile": "指定された Client.txt が見つかりません。",
    "status_off": "通知: OFF (クリックして起動)",
    "status_on": "通知: ON (監視中...)",
    "discord_msg": "💀 **【PoE2 死亡通知】**\nプレイヤー「**{name}**」が死亡しました！",
    "test_msg": "✅ **【PoE2 死亡通知ツール】**\nWebhookの接続テストに成功しました！ツールは正常に連動しています。",
    "test_success": "テストメッセージを送信しました。Discordを確認してください。",
    "test_fail": "送信に失敗しました。URLが正しいか確認してください。\nエラー: {err}",
}

DEFAULT_PATHS = {
    "Steam": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Path of Exile 2\\logs\\Client.txt",
    "Standalone": "C:\\Program Files (x86)\\Grinding Gear Games\\Path of Exile 2\\logs\\Client.txt",
}


class DeathNotifierApp:

    def __init__(self, root):
        self.root = root
        self.is_running = False
        self.log_thread = None

        self.config = self.load_config()
        self.game_lang = self.config.get("game_lang", "日本語")

        self.root.title(TEXTS["title"])
        self.root.geometry("520x460")  # チェックボックス等の追加に伴い少し縦幅を広げました

        self.create_widgets()
        self.auto_detect_path()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        t = TEXTS

        # --- ゲーム内言語選択 ---
        frame_meta = tk.Frame(self.root)
        frame_meta.pack(fill="x", padx=20, pady=(10, 0))

        tk.Label(frame_meta, text=t["lang_lbl"]).pack(side="left")
        self.cmb_lang = ttk.Combobox(
            frame_meta, values=["日本語", "English"], width=10, state="readonly"
        )
        self.cmb_lang.set(self.game_lang)
        self.cmb_lang.bind("<<ComboboxSelected>>", self.on_lang_change)
        self.cmb_lang.pack(side="left", padx=5)

        # --- プラットフォーム選択 ---
        tk.Label(self.root, text=t["platform"]).pack(
            anchor="w", padx=20, pady=(10, 0)
        )
        self.cmb_platform = ttk.Combobox(
            self.root, values=["Steam", "Standalone"], state="readonly"
        )
        self.cmb_platform.set(self.config.get("platform", "Steam"))
        self.cmb_platform.bind("<<ComboboxSelected>>", self.on_platform_change)
        self.cmb_platform.pack(fill="x", padx=20, pady=5)

        # --- Webhook テストボタン (ご要望により入力欄の上に追加) ---
        frame_webhook_top = tk.Frame(self.root)
        frame_webhook_top.pack(fill="x", padx=20, pady=(10, 0))

        tk.Label(frame_webhook_top, text=t["webhook"]).pack(side="left")
        btn_test = tk.Button(
            frame_webhook_top,
            text=t["test_btn"],
            command=self.test_webhook,
            font=("Arial", 9),
            bg="#f0f0f0",
        )
        btn_test.pack(side="right")

        # --- Webhook URL 入力欄 ---
        self.ent_webhook = tk.Entry(self.root)
        self.ent_webhook.insert(0, self.config.get("webhook_url", ""))
        self.ent_webhook.pack(fill="x", padx=20, pady=5)

        # --- Client.txt パス ---
        tk.Label(self.root, text=t["logpath"]).pack(
            anchor="w", padx=20, pady=(10, 0)
        )
        self.ent_logpath = tk.Entry(self.root)
        self.ent_logpath.insert(0, self.config.get("log_path", ""))
        self.ent_logpath.pack(fill="x", padx=20, pady=5)

        # --- スクショ送信有効化チェックボックス ---
        self.var_send_ss = tk.BooleanVar()
        self.var_send_ss.set(self.config.get("send_screenshot", True))
        chk_ss = tk.Checkbutton(
            self.root, text=t["send_ss_lbl"], variable=self.var_send_ss
        )
        chk_ss.pack(anchor="w", padx=20, pady=10)

        # --- 保存ボタン ---
        btn_save = tk.Button(self.root, text=t["save_btn"], command=self.save_config)
        btn_save.pack(pady=5)

        ttk.Separator(self.root, orient="horizontal").pack(
            fill="x", padx=20, pady=10
        )

        # --- ON/OFF ボタン ---
        btn_text = t["status_on"] if self.is_running else t["status_off"]
        btn_color = "green" if self.is_running else "red"
        self.btn_toggle = tk.Button(
            self.root,
            text=btn_text,
            bg=btn_color,
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.toggle_monitoring,
        )
        self.btn_toggle.pack(pady=5, ipady=5, ipadx=10)

    def auto_detect_path(self):
        if not self.ent_logpath.get():
            for platform, path in DEFAULT_PATHS.items():
                if os.path.exists(path):
                    self.cmb_platform.set(platform)
                    self.ent_logpath.delete(0, tk.END)
                    self.ent_logpath.insert(0, path)
                    break

    def on_platform_change(self, event):
        platform = self.cmb_platform.get()
        self.ent_logpath.delete(0, tk.END)
        self.ent_logpath.insert(0, DEFAULT_PATHS[platform])

    def on_lang_change(self, event):
        self.game_lang = self.cmb_lang.get()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_config(self):
        self.config["game_lang"] = self.cmb_lang.get()
        self.config["platform"] = self.cmb_platform.get()
        self.config["webhook_url"] = self.ent_webhook.get().strip()
        self.config["log_path"] = self.ent_logpath.get().strip()
        self.config["send_screenshot"] = self.var_send_ss.get()

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Success", TEXTS["save_success"])

    def test_webhook(self):
        url = self.ent_webhook.get().strip()
        if not url:
            messagebox.showerror("Error", "Webhook URLを入力してください。")
            return
        try:
            res = requests.post(url, json={"content": TEXTS["test_msg"]})
            if res.status_code in [200, 204]:
                messagebox.showinfo("Success", TEXTS["test_success"])
            else:
                messagebox.showerror(
                    "Error", TEXTS["test_fail"].format(err=res.status_code)
                )
        except Exception as e:
            messagebox.showerror("Error", TEXTS["test_fail"].format(err=str(e)))

    def toggle_monitoring(self):
        t = TEXTS
        if not self.is_running:
            webhook = self.ent_webhook.get().strip()
            log_path = self.ent_logpath.get().strip()

            if not webhook or not log_path:
                messagebox.showerror("Error", t["err_input"])
                return
            if not os.path.exists(log_path):
                messagebox.showerror("Error", t["err_nofile"])
                return

            self.is_running = True
            self.btn_toggle.config(text=t["status_on"], bg="green")

            self.log_thread = threading.Thread(
                target=self.watch_log, args=(log_path, webhook), daemon=True
            )
            self.log_thread.start()
        else:
            self.is_running = False
            self.btn_toggle.config(text=t["status_off"], bg="red")

    def watch_log(self, log_path, webhook_url):
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            f.seek(0, os.SEEK_END)
            while self.is_running:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue

                current_setting = self.game_lang
                is_dead = False
                char_name = ""

                # --- 日本語設定のとき ---
                if current_setting == "日本語" and "が死亡しました。" in line:
                    match = re.search(r"(\w+)が死亡しました", line)
                    if match:
                        char_name = match.group(1)
                        is_dead = True

                # --- 英語設定のとき ---
                elif current_setting == "English" and (
                    "has been slain" in line or "is now dead" in line
                ):
                    match = re.search(
                        r"(\w+)\s(?:has\sbeen\sslain|is\snow\sdead)", line
                    )
                    if match:
                        char_name = match.group(1)
                        is_dead = True

                if is_dead:
                    # ログ検知後の処理（5秒待機＆スクショ撮影＆Discord送信）を丸ごと別スレッドへ投げる
                    # これにより、待機中もゲームログの監視が止まらず動き続けます
                    threading.Thread(
                        target=self.delayed_alert,
                        args=(webhook_url, char_name),
                        daemon=True,
                    ).start()

    def delayed_alert(self, webhook_url, char_name):
        # 死亡検知から指定の秒数（5秒）だけ待機
        time.sleep(5.0)

        # 5秒経った「今」の画面をスクショ撮影
        screenshot_bytes = None
        if self.var_send_ss.get():
            screenshot_bytes = self.capture_poe2_window()

        # Discordへアラートを送信
        self.trigger_alert(webhook_url, char_name, screenshot_bytes)

    def capture_poe2_window(self):
        try:
            # 「Path of Exile 2」というタイトルのウィンドウを探す
            windows = gw.getWindowsWithTitle("Path of Exile 2")
            if windows:
                poe_win = windows[0]
                # 最小化されていなければ位置を取得
                if not poe_win.isMinimized:
                    # ウィンドウの座標(左, 上, 右, 下)を取得してキャプチャ
                    bbox = (
                        poe_win.left,
                        poe_win.top,
                        poe_win.right,
                        poe_win.bottom,
                    )
                    img = ImageGrab.grab(bbox)

                    # メモリ上でJPEGに変換
                    output = BytesIO()
                    img.convert("RGB").save(output, format="JPEG", quality=85)
                    return output.getvalue()
            # 見つからない、または最小化時は画面全体を撮影
            img = ImageGrab.grab()
            output = BytesIO()
            img.convert("RGB").save(output, format="JPEG", quality=85)
            return output.getvalue()
        except Exception as e:
            print(f"Screenshot Error: {e}")
            return None

    def trigger_alert(self, webhook_url, char_name, screenshot_bytes):
        message = TEXTS["discord_msg"].format(name=char_name)
        try:
            if screenshot_bytes:
                # テキストとJPEG画像を同時にWebhookで送信
                payload = {"content": message}
                files = {
                    "file": (
                        f"{char_name}_rip.jpg",
                        screenshot_bytes,
                        "image/jpeg",
                    )
                }
                requests.post(webhook_url, data=payload, files=files)
            else:
                # 画像がない、またはチェックOFF時はテキストのみ
                requests.post(webhook_url, json={"content": message})
        except Exception as e:
            print(f"Discord Send Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DeathNotifierApp(root)
    root.mainloop()