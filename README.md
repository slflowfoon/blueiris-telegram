# blueiris-telegram

Python script to send alert image to Telegram along side [slflowfoon/blueiris-llm](https://github.com/slflowfoon/blueiris-llm)

## Step 1: Installation

Place the following file in a folder named after the camera, for example, `C:\Users\MyUser\Documents\Blue Iris\Driveway\`:
  * `__init__.py`

1. In Blue Iris, create the following action on alert:
   * **Action:** `Run program/script`
   * **File:** `C:\Users\MyUser\Documents\Telegram\__init__.py`
   * **Parameters:** `--response "%1" --img_path "D:\Directory\Where\Alert\Images\Are\Saved\&ALERT_PATH"`
     * **Tip:** `--response "%1"` can be changed for `--response "&MEMO"` if you're not using [slflowfoon/blueiris-llm](https://github.com/slflowfoon/blueiris-llm)
   * **Camera:** Choose the camera your are setting up, for example, `Driveway`
     
<p align="center"><img src="https://github.com/slflowfoon/blueiris-telegram/blob/main/images/Notification%201.png?raw=true" width=500 /></p>

### Step 2: Required Script Configuration in `__init__.py`

https://smarthomepursuits.com/how-to-setup-a-telegram-bot/
1. `TELEGRAM_API_KEY`
2. `CHAT_ID`

----
