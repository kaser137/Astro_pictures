import os
import argparse
import dotenv
from pathlib import Path
from service_functions import publish_images_to_telegram


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    bot_token = os.getenv('KASER_TELEGRAM_TOKEN')
    chat_id = os.getenv('KASER_TG_CHAT_ID')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--period', help='number of seconds', type=int, default=14400)
    parser.add_argument('-i', '--image', help='path/name_image', default=None)
    parser = parser.parse_args()
    period = parser.period
    picture = parser.image
    publish_images_to_telegram(bot_token, chat_id, 'images', period=period, picture=picture)


if __name__ == '__main__':
    main()
