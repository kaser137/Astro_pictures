import dotenv
import os
import argparse
from service_functions import output_images_to_telegram

dotenv.load_dotenv('venv/.env')
token_bot = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--period', help='number of seconds', type=int, default=14400)

parser.add_argument('-i', '--image', help='path/name_image', default=None)
parser = parser.parse_args()
period = parser.period
picture = parser.image

output_images_to_telegram(token_bot, chat_id, 'images', period=period, picture=picture)
