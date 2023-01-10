import requests
import urllib.parse
import os.path
import dotenv
import datetime


def ext_file(url):
    path = urllib.parse.urlsplit(urllib.parse.unquote(url)).path
    *_, ext = os.path.splitext(path)
    return ext


def grab_img(url, path):
    if ext_file(url):
        response = requests.get(url)
        response.raise_for_status()
        with open(path, 'wb') as file:
            file.write(response.content)


def fetch_spacex_last_launch(id_launch='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{id_launch}'
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs('./images/spaceX', exist_ok=True)
    images_links = response.json()['links']['flickr']['original']
    for path in images_links:
        grab_img(path, './images/spaceX/' + path.split('/')[-1])


def get_nasa_pict(token, count=1):
    response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': f'{token}', 'count': f'{count}'})
    response.raise_for_status()
    os.makedirs('./images/nasa', exist_ok=True)
    images_links = [i['url'] for i in response.json()]
    for path in images_links:
        grab_img(path, './images/nasa/' + path.split('/')[-1])


def get_nasa_epic(token):
    response = requests.get('https://epic.gsfc.nasa.gov/api/natural', params={'api_key': f'{token}'})
    response.raise_for_status()
    os.makedirs('./images/nasaEpic', exist_ok=True)
    images_links = [
        'https://epic.gsfc.nasa.gov/archive/natural/' + datetime.datetime.fromisoformat(i['date']).strftime(
            '%Y/%m/%d/') + 'png/' + i['image'] + '.png' for i in response.json()]
    for path in images_links:
        if ext_file(path):
            response = requests.get(path, params={'api_key': f'{token}'})
            response.raise_for_status()
            with open('./images/nasaEpic/' + path.split('/')[-1], 'wb') as file:
                file.write(response.content)


if __name__ == '__main__':
    dotenv.load_dotenv('venv/.env')
    num_launch = '5eb87d47ffd86e000604b38a'
    token_user = os.getenv('NASA_TOKEN')
    fetch_spacex_last_launch(num_launch)
    get_nasa_pict(token_user, 3)
    get_nasa_epic(token_user)
