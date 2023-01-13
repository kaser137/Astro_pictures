import requests
import urllib.parse
import os
import telegram
import time
import random
from PIL import Image


def get_ext_file(url):
    path = urllib.parse.urlsplit(urllib.parse.unquote(url)).path
    *_, ext = os.path.splitext(path)
    return ext


def grab_img(url, name_for_img):
    if get_ext_file(url):
        response = requests.get(url)
        response.raise_for_status()
        with open(name_for_img, 'wb') as file:
            file.write(response.content)


def adjust_size_image(image):
    size_image = os.path.getsize(image)
    if size_image >= 20000000:
        ratio_size = 20000000 / size_image
        image_pil = Image.open(image)
        width, height = image_pil.size
        image_pil.thumbnail((int(width*ratio_size), int(height*ratio_size)))
        image_pil.save(image)
        image_pil.close()
    return image


def output_images_to_telegram(token, chat_id, dir_pictures, period=14400):
    list_of_pictures = []
    for root, dirs, files in os.walk(dir_pictures):
        for name in files:
            full_name = os.path.join(root, name)
            adjust_size_image(full_name)
            list_of_pictures.append(full_name)
    bot = telegram.Bot(token=token)
    while True:
        random_index = random.randint(0, len(list_of_pictures) - 1)
        bot.send_document(chat_id=chat_id, document=open(list_of_pictures[random_index], 'rb'))
        time.sleep(period)
