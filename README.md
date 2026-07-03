# PoE2 RIP Notification Tool

Path of Exile 2 (PoE2) 用の死亡通知＆スクリーンショット送信ツールです。

<img width="473" height="72" alt="TOPnotifichation" src="https://github.com/user-attachments/assets/0f9c4433-51ce-495a-96d1-6779bad9ade6" />

<img width="2523" height="1039" alt="TOPRIP" src="https://github.com/user-attachments/assets/fd02229b-07d7-4c0b-a2d3-08cb02c91e64" />



## 概要
ハードコア（HC）モードでキャラクターが死亡した際、自動的に検知してDiscordの指定チャンネルへ通知とスクリーンショットを送信します。仲間との「死に様」の共有や、死因の特定にご活用ください。

**※重要：対応モードについて**
本ツールはハードコアモードでの利用を主目的としていますが、ゲームの仕様上、ソフトコア・ハードコアの区別なく「キャラクターが死亡した」というログを検知します。ソフトコアモードでプレイしている際も死亡時に通知が送信されますので、適宜ツールのON/OFFを切り替えてご使用ください。

> **※注意 / Note:** > 本ツールのUIは日本語のみですが、ゲーム側の言語設定は日本語・英語の両方に対応しています。

### 主な機能
1. **死亡検知アラート**
   - キャラクターの死亡ログをリアルタイムで検知し、Discordへ即時通知します。
2. **5秒遅延スクリーンショット送信**
   - ログ検知から5秒後にゲーム画面を自動キャプチャし、Discordへ送信します。
   - 力尽きた瞬間のドラマチックな光景や、敗因分析のための貴重な記録をきれいな画質で残せます。
   - **ハードコアモードでは「散り際」こそが、最も輝く瞬間です。その一瞬をぜひ逃さず記録してください。**
     
## 使い方

1. `PoE2_Death_Tool_v2.exe` を起動します。

   <img width="493" height="470" alt="setting" src="https://github.com/user-attachments/assets/4ff7b352-925a-448f-9659-c229884fd702" />


2. クライアントの言語設定、プレイするプラットフォーム（Steam/Standalone）を選択します。
3. DiscordのWebhook URLを設定します。
   >Webhook URLの取得方法は下記となります。

   **■ 事前準備（Discord側の設定）**
   本ツールを使用するには、Discordの「ウェブフック URL」が必要です。

   1. 通知を送りたいDiscordサーバーのチャンネル設定（歯車マーク）を開きます。
   
      <img width="308" height="63" alt="textchannelsetting" src="https://github.com/user-attachments/assets/02900ab9-cc3d-469a-99b2-8a2fde859478" />

      
   
   2. 「連携サービス」＞「ウェブフック」＞「ウェブフックを作成」をクリックします。
      　生成された「ウェブフック URL」をコピーします。
      <img width="940" height="277" alt="inetegration" src="https://github.com/user-attachments/assets/025ff54d-e4db-4833-be2e-16a4c61cfd45" />
　　　 
      <img width="668" height="398" alt="webhookURL" src="https://github.com/user-attachments/assets/2e59f3e7-cec0-4770-8292-727ea9a67fd3" />

   ※フレンドのサーバーで使いたい場合：サーバーの管理者権限が必要です。管理者であるフレンドの方に「ウェブフックのURLを作って教えて！」と頼んでみてください。

4. ウェブフックURLをペーストし、Webhookテスト送信ボタンを押して設定したディスコードのサーバーに下記の通知が来ればWebhookの設定は完了です。

   　<img width="516" height="77" alt="webhookURL2" src="https://github.com/user-attachments/assets/087f7642-272d-47d5-9ae5-eae3c98adbad" />

　　　<img width="304" height="76" alt="webhooktest" src="https://github.com/user-attachments/assets/537abd10-8090-434f-a484-880f78a4c026" />

   
5. 【通知】ボタンを押して監視を開始します。

   <img width="277" height="116" alt="notificatioONOFF" src="https://github.com/user-attachments/assets/72021edd-d5b1-4773-b2ac-c265c01e048a" />


* **画面設定:** スクリーンショット機能は【ウィンドウ】または【仮想フルスクリーン】モードで動作します。
 > **※注意:** > スクリーンショットは死亡検知の **5秒後** に撮影されます。

## 既知の問題

本ツールは「Client.txt」のログを監視して通知を行う仕組みのため、以下の条件下で誤検知が発生する可能性があります。

1. **文字列の誤検知**: チャット欄などで特定のキーワードが含まれた場合、死亡通知として誤って検知される場合があります。
2. **パーティプレイ時の挙動（未確認）**: パーティメンバーが死亡した際、ログの仕様上、自分以外のメンバーの死亡ログも検知して通知を送ってしまう可能性があります。こちらについてはまだ完全には検証できておりませんが、可能性として共有させていただきます。

※現在、これらは仕様上の制限として認識しており、今後のアップデートで精度の向上を検討中です。

## 免責事項
本ツールは非公式ツールです。使用により生じたトラブルやゲームアカウント停止等の損害に対し、作成者は一切責任を負いません。ご利用は自己責任でお願いします。

---

## English (Translation)

This is a support tool for Path of Exile 2 (PoE2) that automatically sends a death notification and a screenshot to your Discord channel when your character dies.

### Key Features
1. **Death Detection Alert**
   - Detects your character's death log in real-time and sends an instant notification to Discord.
2. **5-Second Delayed Screenshot**
   - Automatically captures your game screen 5 seconds after the death detection and sends it to Discord.
   - It captures the dramatic moment of your defeat in high quality, perfect for reliving the experience or analyzing what went wrong.
   - **In Hardcore mode, your final moments are when you shine the brightest. Don't let that moment fade away—capture it.**

**Note: Compatibility**
While this tool is primarily designed for Hardcore (HC) mode, it detects any "character death" event from the game logs. Please note that it will also trigger notifications during Softcore play. You can toggle the tool ON/OFF manually depending on your current mode.

### How to use
1. Run `PoE2_Death_Tool_v2.exe`.

   <img width="493" height="470" alt="setting" src="https://github.com/user-attachments/assets/4ff7b352-925a-448f-9659-c229884fd702" />

2. Choose your game language and platform (Steam/Standalone).
3. Set your Discord Webhook URL.

   How to get your Webhook URL:

   **■ Discord Server Settings**
   To use this tool, you need a "Webhook URL" from Discord.

   1. Open the channel settings (gear icon) of the Discord server where you want to receive notifications.
      <img width="308" height="63" alt="textchannelsetting" src="https://github.com/user-attachments/assets/59cc7e16-fffc-4812-9767-b88adaf4caa6" />


   2. Go to "Integrations" > "Webhooks" > "New Webhook" and copy the generated "Webhook URL".
      <img width="940" height="277" alt="inetegration" src="https://github.com/user-attachments/assets/86472d0e-e19c-4ae4-b958-8d46dfa594b9" />
      <img width="668" height="398" alt="webhookURL" src="https://github.com/user-attachments/assets/93ddcff7-d57f-4b93-8797-876e4790f867" />




      
      ※ If you want to use it on a friend's server: You need administrator permissions for the server. Please ask the server administrator (your friend) to create a Webhook URL and share it with you.

   *Note: The screenshots are in Japanese, but the button locations and procedures are identical regardless of your Discord language settings.*

4. Paste your Webhook URL into the tool and click the "Webhook Test" button. If you receive the notification below in your Discord server, the setup is complete.

   <img width="516" height="77" alt="webhookURL2" src="https://github.com/user-attachments/assets/958a8250-17be-45b7-922b-881d4c5a302b" />

   
      <img width="304" height="76" alt="webhooktest" src="https://github.com/user-attachments/assets/a09f2b6e-8ccc-4356-a95e-8616ff2a5dd4" />



5. Click the "ON" button to start monitoring.

   <img width="277" height="116" alt="notificatioONOFF" src="https://github.com/user-attachments/assets/d6304e37-d6ba-4d6f-a42a-ee27e396e07e" />

### Important Notes
* **In-Game Screen Mode:** The screenshot feature requires the game's display setting to be set to either "Windowed" or "Windowed Fullscreen" mode.
> **※Note:** > Screenshots are taken 5 seconds after the death is detected.

## Known Issues

Due to the nature of how this tool monitors the "Client.txt" log file, false positives may occur under the following conditions:

1. **Text Detection**: If specific keywords appear in the chat or other logs, the tool may mistakenly trigger a death notification.
2. **Party Play (Unconfirmed)**: It is possible that the tool may also detect the death of a party member and report it as your own. This has not been fully verified yet, but I wanted to make users aware of the possibility.

*These issues are currently recognized as limitations of the tool's design, and I am considering potential improvements for future updates.*

## Disclaimer
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
