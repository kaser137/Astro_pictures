import requests
import os
import dotenv
from pathlib import Path
from service_functions import grab_img


def get_nasa_pictures(token, count=1):
    response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': f'{token}', 'count': f'{count}'})
    response.raise_for_status()
    os.makedirs(Path('images', 'nasa'), exist_ok=True)
    images_links = [i['url'] for i in response.json() if i['media_type'] == 'image']
    for path in images_links:
        grab_img(path, Path('images', 'nasa', Path(path).parts[-1]))


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    nasa_token = os.getenv('KASER_NASA_TOKEN')
    get_nasa_pictures(nasa_token, 30)


if __name__ == '__main__':
    main()
