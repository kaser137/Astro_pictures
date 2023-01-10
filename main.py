import os.path
import dotenv
from fetch_spacex_last_launch import fetch_spacex_last_launch
from get_nasa_pictures import get_nasa_pictures
from get_epic_nasa import get_epic_nasa


dotenv.load_dotenv('venv/.env')
id_for_example = '5eb87d47ffd86e000604b38a'
token_user = os.getenv('NASA_TOKEN')
fetch_spacex_last_launch(id_for_example)
get_nasa_pictures(token_user, 3)
get_epic_nasa(token_user)
