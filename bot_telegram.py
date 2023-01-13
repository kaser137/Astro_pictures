import dotenv
import os
import argparse
from service_functions import output_images_to_telegram

dotenv.load_dotenv('venv/.env')
token_bot = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
parser = argparse.ArgumentParser('This function outputs pictures to Telegram chat with period "period" in secs, '
                                 'if omitted, period = 4 hours ')
parser.add_argument('period')
parser = parser.parse_args()
period = int(parser.period)
output_images_to_telegram(token_bot, chat_id, 'images', period=period)
