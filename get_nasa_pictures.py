import requests
import os
import dotenv
from service_functions import grab_img


def get_nasa_pictures(token, count=1):
    response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': f'{token}', 'count': f'{count}'})
    response.raise_for_status()
    os.makedirs('./images/nasa', exist_ok=True)
    images_links = [i['url'] for i in response.json()]
    for path in images_links:
        grab_img(path, './images/nasa/' + path.split('/')[-1])


if __name__ == '__main__':
    dotenv.load_dotenv('venv/.env')
    token_user = os.getenv('NASA_TOKEN')
    get_nasa_pictures(token_user, 3)
