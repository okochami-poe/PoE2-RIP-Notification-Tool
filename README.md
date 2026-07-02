# PoE2 RIP Notification Tool

Path of Exile 2 (PoE2) 用の死亡通知＆スクリーンショット送信ツールです。

<img width="600" height="301" alt="githubtop" src="https://github.com/user-attachments/assets/2f52abac-3f5c-4d3b-9857-dbb31a9d3389" />


## 概要
ハードコア（HC）モードでキャラクターが死亡した際、自動的に検知してDiscordの指定チャンネルへ通知とスクリーンショットを送信します。仲間との「死に様」の共有や、死因の特定にご活用ください。

**※重要：対応モードについて**
本ツールはハードコアモードでの利用を主目的としていますが、ゲームの仕様上、ソフトコア・ハードコアの区別なく「キャラクターが死亡した」というログを検知します。ソフトコアモードでプレイしている際も死亡時に通知が送信されますので、適宜ツールのON/OFFを切り替えてご使用ください。

> **※注意 / Note:** > 本ツールのUIは日本語のみですが、ゲーム側の言語設定は日本語・英語の両方に対応しています。

### 主な機能
* **死亡検知:** 死亡ログを検知しDiscordへ自動通知。
* **5秒遅延スクリーンショット:** 死亡検知の5秒後に自動キャプチャして送信します。

## 使い方

1. `PoE2_Death_Tool_v2.exe` を起動します。
2. DiscordのWebhook URLを設定します。
   <details>
   <summary>Webhook URLの取得方法はこちら (Click to see how to get Webhook URL)</summary>

   **■ 事前準備（Discord側の設定）**
   本ツールを使用するには、Discordの「ウェブフック URL」が必要です。

   1. 通知を送りたいDiscordサーバーのチャンネル設定（歯車マーク）を開きます。
   2. 「連携サービス」＞「ウェブフック」＞「ウェブフックを作成」をクリックします。
   3. 生成された「ウェブフック URL」をコピーして控えておきます。

   ※フレンドのサーバーで使いたい場合：
   サーバーの管理者権限が必要です。管理者であるフレンドの方に「ウェブフックのURLを作って教えて！」と頼んでみてください。
   </details>
3. プレイするプラットフォーム（Steam/Standalone）を選択します。
4. 【通知: ON】ボタンを押して監視を開始します。

* **画面設定:** スクリーンショット機能は【ウィンドウ】または【仮想フルスクリーン】モードで動作します。
 > **※注意:** > スクリーンショットは死亡検知の **5秒後** に撮影されます。

**【設定画面】**

<img width="493" height="470" alt="setting" src="https://github.com/user-attachments/assets/4ff7b352-925a-448f-9659-c229884fd702" />

## 免責事項
本ツールは非公式ツールです。使用により生じたトラブルやゲームアカウント停止等の損害に対し、作成者は一切責任を負いません。ご利用は自己責任でお願いします。

---

## English (Translation)

This is a support tool for Path of Exile 2 (PoE2) that automatically sends a death notification and a screenshot to your Discord channel when your character dies.

**Note: Compatibility**
While this tool is primarily designed for Hardcore (HC) mode, it detects any "character death" event from the game logs. Please note that it will also trigger notifications during Softcore play. You can toggle the tool ON/OFF manually depending on your current mode.

### How to use
1. Run `PoE2_Death_Tool_v2.exe`.
2. Set your Discord Webhook URL.

   <details>
   <summary>Click here to see how to get your Webhook URL</summary>

   **■ Discord Server Settings**
   To use this tool, you need a "Webhook URL" from Discord.

   1. Open the channel settings (gear icon) of the Discord server where you want to receive notifications.
   2. Go to "Integrations" > "Webhooks" > "New Webhook".
   3. Copy the generated "Webhook URL".

   **※ If you want to use it on a friend's server:**
   You need administrator permissions for the server. Please ask the server administrator (your friend) to create a Webhook URL and share it with you.
   </details>
3. Select your platform (Steam or Standalone).
4. Click the "ON" button to start monitoring.
### Important Notes
* **In-Game Screen Mode:** The screenshot feature requires the game's display setting to be set to either "Windowed" or "Windowed Fullscreen" mode.
> **※Note:** > Screenshots are taken 5 seconds after the death is detected.
### Disclaimer
This is an unofficial tool. The author is not responsible for any issues, including account bans or technical problems, caused by using this tool. Use it at your own risk.

> The UI of this tool is in Japanese only, but it is compatible with both "Japanese" and "English" in-game language settings.

---

## ライセンス・著作権 / Credits & Licenses
各ライブラリのライセンスに基づき利用しています。
- Pillow: [HPND License](https://github.com/python-pillow/Pillow)
- Requests: [Apache License 2.0](https://github.com/psf/requests)
- PyGetWindow: [BSD 3-Clause License](https://github.com/asweigart/PyGetWindow)

---
*詳細は同梱の README.txt をご覧ください。 / Please refer to README.txt for more details.*
