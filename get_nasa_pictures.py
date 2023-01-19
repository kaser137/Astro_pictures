import os
import dotenv
from pathlib import Path
from service_functions import grab_img, api_request


def get_nasa_pictures(token, count=1):
    response = api_request('https://api.nasa.gov/planetary/apod', payload={'api_key': f'{token}', 'count': f'{count}'})
    os.makedirs(Path('images', 'nasa'), exist_ok=True)
    images_links = [api_answer['url'] for api_answer in response.json() if api_answer['media_type'] == 'image']
    for path in images_links:
        grab_img(path, Path('images', 'nasa', Path(path).parts[-1]), payload={'api_key': f'{token}'})


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    nasa_token = os.environ.get('NASA_TOKEN')
    get_nasa_pictures(nasa_token, 3)


if __name__ == '__main__':
    main()
