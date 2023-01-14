import os
import dotenv
from fetch_spacex_last_launch import fetch_spacex_last_launch
from get_nasa_pictures import get_nasa_pictures
from get_epic_nasa import get_epic_nasa


dotenv.load_dotenv('venv/.env')
id_for_example = '5eb87d47ffd86e000604b38a'
token_nasa = os.getenv('NASA_TOKEN')
token_bot = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
dir_pictures = 'images'
count = input('Input number of pictures from NASA, what should you get. For 1 picture, press Enter:')
fetch_spacex_last_launch(id_for_example)
if count:
    get_nasa_pictures(token_nasa, int(count))
else:
    get_nasa_pictures(token_nasa)
get_epic_nasa(token_nasa)
