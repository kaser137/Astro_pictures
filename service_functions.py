import requests
import os
import telegram
import time
import random
from PIL import Image


def request_api(url, payload=None, attempt_timeout=10):
    flag = True
    while flag:
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            flag = False
            return response
        except requests.exceptions.ConnectionError or requests.exceptions.Timeout:
            print(f'connection failed, next attempt in {attempt_timeout} seconds')
            time.sleep(attempt_timeout)


def grab_img(url, name_for_img, payload=None):
    response = request_api(url, payload)
    with open(name_for_img, 'wb') as file:
        file.write(response.content)


def adjust_size_image(fullpath):
    size_image = os.path.getsize(fullpath)
    if size_image >= 20000000:
        ratio_size = 20000000 / size_image
        with Image.open(fullpath) as image_pil:
            width, height = image_pil.size
            image_pil.thumbnail((int(width * ratio_size), int(height * ratio_size)))
            image_pil.save(fullpath)
    return fullpath


def collect_img_from_dir(dir_pictures):
    image_path_list = []
    for root, dirs, files in os.walk(dir_pictures):
        for name in files:
            full_name = os.path.join(root, name)
            adjust_size_image(full_name)
            image_path_list.append(full_name)
    return image_path_list


def send_document(token, chat_id, document):
    bot = telegram.Bot(token=token)
    with open(document, 'rb') as document:
        bot.send_document(chat_id=chat_id, document=document)


def publish_images_to_telegram(token, chat_id, dir_pictures, period=14400, attempt_timeout=20):
    while True:
        try:
            image_path_list = collect_img_from_dir(dir_pictures)
            send_document(token, chat_id, random.choice(image_path_list))
            time.sleep(period)
        except telegram.error.NetworkError:
            print(f'connection failed, next attempt in {attempt_timeout} seconds')
            time.sleep(attempt_timeout)
