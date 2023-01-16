import requests
import os
import datetime
import dotenv
from pathlib import Path
from service_functions import grab_img


def get_epic_nasa(token):
    payload = {'api_key': f'{token}'}
    response = requests.get('https://epic.gsfc.nasa.gov/api/natural', params=payload)
    response.raise_for_status()
    os.makedirs(Path('images', 'nasaEpic'), exist_ok=True)
    images_links = [os.path.join(
        'https://epic.gsfc.nasa.gov/archive/natural/', datetime.datetime.fromisoformat(i['date']).strftime(
            '%Y/%m/%d/'), 'png/', f'{i["image"]}.png') for i in response.json()]
    for path in images_links:
        grab_img(path, Path('images', 'nasaEpic', Path(path).parts[-1]), payload)


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    nasa_token = os.getenv('KASER_NASA_TOKEN')
    get_epic_nasa(nasa_token)


if __name__ == '__main__':
    main()
