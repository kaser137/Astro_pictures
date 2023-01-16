import requests
import os.path
import argparse
from pathlib import Path
from service_functions import grab_img


def fetch_spacex_last_launch(start_id='latest'):
    url = f'https://api.spacexdata.com/v5/launches/{start_id}'
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(Path('images', 'spaceX'), exist_ok=True)
    images_links = response.json()['links']['flickr']['original']
    for path in images_links:
        grab_img(path, Path('images', 'spaceX', Path(path).parts[-1]))


def main():
    parser = argparse.ArgumentParser('This function fetches pictures from specified launch of Space X, if given, '
                                     'or latest launch if omitted')
    parser.add_argument('id_launch')
    id_launch = parser.parse_args().id_launch
    fetch_spacex_last_launch(id_launch)


if __name__ == '__main__':
    main()
