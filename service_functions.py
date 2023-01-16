import requests
import os
import telegram
import time
import random
from PIL import Image


def grab_img(url, name_for_img, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(name_for_img, 'wb') as file:
        file.write(response.content)


def adjust_size_image(image):
    size_image = os.path.getsize(image)
    if size_image >= 20000000:
        ratio_size = 20000000 / size_image
        with Image.open(image) as image_pil:
            width, height = image_pil.size
            image_pil.thumbnail((int(width * ratio_size), int(height * ratio_size)))
            image_pil.save(image)
    return image


def collect_img_from_dir(dir_pictures):
    list_of_pictures = []
    for root, dirs, files in os.walk(dir_pictures):
        for name in files:
            full_name = os.path.join(root, name)
            adjust_size_image(full_name)
            list_of_pictures.append(full_name)
    return list_of_pictures


def publish_images_to_telegram(token, chat_id, dir_pictures, period=14400, picture=None):
    bot = telegram.Bot(token=token)
    if picture is None:
        list_of_pictures = collect_img_from_dir(dir_pictures)
        while True:
            random_index = random.randint(0, len(list_of_pictures) - 1)
            with open(list_of_pictures[random_index], 'rb') as document:
                bot.send_document(chat_id=chat_id, document=document)
            time.sleep(period)
    else:
        with open(picture, 'rb') as document:
            bot.send_document(chat_id=chat_id, document=document)
