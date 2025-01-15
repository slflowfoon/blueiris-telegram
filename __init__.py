#!/usr/bin/env python

import argparse
import requests

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendPhoto"
TELEGRAM_API_KEY = "REPLACE_WITH_BOT_API_KEY"
CHAT_ID = "REPLACE_WITH_CHAT_ID"

def send_photo_with_caption(img_path, response):
    """Send an image with a text caption to the Telegram chat."""
    try:
        with open(img_path, 'rb') as photo:
            response = requests.post(
                TELEGRAM_API_URL,
                data={
                    'chat_id': CHAT_ID,
                    'caption': response
                },
                files={
                    'photo': photo
                }
            )
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. HTTP Status: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send a text response and image to a Telegram chat.")
    parser.add_argument("--response", required=True, help="Text response to send.")
    parser.add_argument("--img_path", required=True, help="Path to the image file.")
    
    args = parser.parse_args()
    
    send_photo_with_caption(args.img_path, args.response)

if __name__ == "__main__":
    main()
