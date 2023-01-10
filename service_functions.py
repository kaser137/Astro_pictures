import requests
import urllib.parse
import os.path


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
