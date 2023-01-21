import os
import datetime
import dotenv
from pathlib import Path
from service_functions import grab_img, api_request


def get_epic_nasa(token):
    response = api_request('https://epic.gsfc.nasa.gov/api/natural', payload={'api_key': f'{token}'})
    os.makedirs(Path('images', 'nasaEpic'), exist_ok=True)
    images_links = [os.path.join(
        'https://epic.gsfc.nasa.gov/archive/natural/', datetime.datetime.fromisoformat(api_answer['date']).strftime(
            '%Y/%m/%d/'), 'png/', f'{api_answer["image"]}.png') for api_answer in response.json()]
    for path in images_links:
        grab_img(path, Path('images', 'nasaEpic', Path(path).parts[-1]), payload={'api_key': f'{token}'})


def main():
    dotenv.load_dotenv(Path('venv', '.env'))
    nasa_token = os.environ['NASA_TOKEN']
    get_epic_nasa(nasa_token)


if __name__ == '__main__':
    main()
