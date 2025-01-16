#!/usr/bin/env python

import os
import subprocess
import argparse


TELEGRAM_BOT_TOKEN = "REPLACE_WITH_BOT_API_KEY"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
CHAT_ID = "REPLACE_WITH_CHAT_ID"


def send_telegram_message_and_photo(api_url, chat_id, text_response, img_path):
    """Sends a message and a photo to the specified Telegram chat."""
    try:
        if not os.path.exists(img_path):
            print(f"Error: Image file not found at {img_path}")
            return

        curl_command = [
            "curl",
            api_url,
            "-F",
            f"chat_id={chat_id}",
            "-F",
            f"photo=@{img_path}",
            "-F",
            f"caption={text_response}",
        ]

        subprocess.run(curl_command, check=True)
        print("Message and Photo sent successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error sending message and photo: {e}")
    except Exception as e:
        print(f"An unexpected error has occurred:{e}")


def main():
    parser = argparse.ArgumentParser(
        description="Send a message and a photo to a Telegram chat."
    )
    parser.add_argument(
        "--response", required=True, help="The text response to send."
    )
    parser.add_argument(
        "--img_path", required=True, help="The path to the image file."
    )

    args = parser.parse_args()

    send_telegram_message_and_photo(
        TELEGRAM_API_URL, CHAT_ID, args.response, args.img_path
    )


if __name__ == "__main__":
    main()
