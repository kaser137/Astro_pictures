import os
import argparse
import dotenv
from pathlib import Path
from service_functions import publish_images_to_telegram


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    bot_token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TG_CHAT_ID')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--period', help='number of seconds', type=int, default=14400)
    parser.add_argument('-i', '--image', help='fullpath of image', default=None)
    parser.add_argument('-t', '--timeout', help='timeout for failed connection (seconds)', type=int, default=20)
    parser = parser.parse_args()
    period = parser.period
    picture = parser.image
    timeout = parser.timeout
    publish_images_to_telegram(bot_token, chat_id, 'images', period=period, picture=picture, attempt_timeout=timeout)


if __name__ == '__main__':
    main()
