import os
import argparse
import dotenv
from pathlib import Path
from service_functions import send_document, publish_images_to_telegram


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    bot_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--period', help='number of seconds', type=int, default=14400)
    parser.add_argument('-i', '--image', help='fullpath of image', default=None)
    parser.add_argument('-t', '--timeout', help='timeout for failed connection (seconds)', type=int, default=20)
    parser = parser.parse_args()
    period = parser.period
    picture = parser.image
    timeout = parser.timeout
    if picture:
        send_document(bot_token, chat_id, picture)
    else:
        publish_images_to_telegram(bot_token, chat_id, 'images', period=period, attempt_timeout=timeout)


if __name__ == '__main__':
    main()
