import requests
import os
import dotenv
import datetime



def get_epic_nasa(token):
    response = requests.get('https://epic.gsfc.nasa.gov/api/natural', params={'api_key': f'{token}'})
    response.raise_for_status()
    os.makedirs('./images/nasaEpic', exist_ok=True)
    images_links = [
        'https://epic.gsfc.nasa.gov/archive/natural/' + datetime.datetime.fromisoformat(i['date']).strftime(
            '%Y/%m/%d/') + 'png/' + i['image'] + '.png' for i in response.json()]
    for path in images_links:
        response = requests.get(path, params={'api_key': f'{token}'})
        response.raise_for_status()
        with open('./images/nasaEpic/' + path.split('/')[-1], 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    dotenv.load_dotenv('venv/.env')
    token_user = os.getenv('NASA_TOKEN')
    get_epic_nasa(token_user)
