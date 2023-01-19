import os
import dotenv
from pathlib import Path
from fetch_spacex_last_launch import fetch_spacex_last_launch
from get_nasa_pictures import get_nasa_pictures
from get_epic_nasa import get_epic_nasa


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    nasa_token = os.environ.get('NASA_TOKEN')
    example_id = '5eb87d47ffd86e000604b38a'
    count = input('Input number of pictures from NASA, what should you get. For 1 picture, press Enter:')
    fetch_spacex_last_launch(example_id)
    if count:
        get_nasa_pictures(nasa_token, int(count))
    else:
        get_nasa_pictures(nasa_token)
    get_epic_nasa(nasa_token)


if __name__ == '__main__':
    main()
