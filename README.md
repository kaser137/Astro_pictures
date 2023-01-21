# Astro_pictures

## What is this?

This project gets pictures from SpaceX and NASA, and then collected pictures publishing in telegram bot 

## How it works?

For working with this project, you have to copy all files in the working directory at your choice.  Create in working 
directory subdirectory "venv" and file ".env" in this subdirectory. In this file, you have to write 3 lines like this:
```python
NASA_TOKEN="4a9a0qp6hW3Bf5oHRiJHiFijgg6tsoasiqKU34IF"
TELEGRAM_TOKEN="5891540462:AAEK9XHL5ylR6r1AnN9Roj5wcTR6jZYlv98"
TG_CHAT_ID="@Pinky_hippo"
```
(presented values is not correct, it's just for example)
Where NASA_TOKEN is your token for API NASA, TELEGRAM_TOKEN is your token for your bot in Telegram, TG_CHAT_ID is your 
chat, in which your telegram bot has administrator's rights.

Python3 should  already be installed. Then use pip (or pip3, if there is a conflict with Python2) to install
dependencies: `pip install -r requirements.txt`

Start file `collect_pictures.py`, it makes directory 'images' in your working directory, then downloads photos from
launches of SpaceX and from NASA in the "images" (follow instruction). If "images" appeared, it means all is OK.

In command line from working directory, type: `python bot_telegram.py [-p] period [-i] image [-t] timeout`, 
where "period"(number of seconds) is period of publishing photos in Telegram (default: 14400 = 4 hours), "image" is 
fullname of pictures from your collection (default: None, but if it occurs program publish this image once), "timeout"
is time in seconds (default: 20 seconds), to next attempt, if connection failed. If you get a picture in your chat, 
after start `bot_telegram.py`, it means all is OK.

## Content:

`fetch_spacex_last_launch.py` contents `fetch_spacex_last_launch(id_launch='latest')`, this function gets pictures from 
launches of SpaceX. Its argument is ID of launch, if omitted, it takes the latest launch.

`get_nasa_pictures.py` contents `get_nasa_pictures(token, count=1)`, this function gets random pictures from NASA 
archive. Arguments are: "token" - user's token for API NASA, and "count": - number of pictures for download. 
If omitted, equal 1.

`get_nasa_epic.py` contents `get_nasa_epic(token)`, this function gets pictures from NASA's project EPIC. 
Argument is "token" - user's token for API NASA.

`service_functions.py` contents:
1. `request_api(url, payload=None, attempt_timeout=10)`, this function makes request to API and, if connection failed,
repeats it after "attempt_timeout" (default = 10 seconds).
2. `grab_img(url, name_for_img)`, this function fetches a file from "URL" and save it as "name_for_img".
3. `adjust_size_image(image)`, this function check size of "image", and if it is more, than 20 MB, reduce size.
4. `collect_img_from_dir(dir_pictures)`, this function takes images from "dir_pictures" and its subdirectories, and 
returns a list of images.
5. `send_document(token, chat_id, document)`, this function send "document" to the Telegram chat (with "chat_id"), 
"token" is your token for telegram bot
6. `publish_images_to_telegram(token, chat_id, dir_pictures, period=14400, attempt_timeout=20)`, this
function periodical publishes random photo from directory "dir_picture". The "token" is your token for telegram bot, 
"chat_id" is ID for your chat, where your bot is administrator, "period" is period of publishing in seconds (default: 
14400 seconds=4 hours), if connection failed, next attempt repeats after "attempt_timeout" (default=20 seconds). 

About `collect_pictures.py` and `bot_telegram.py` was said upper, in "How it works?".

Код написан в образовательных целях на курсах для веб-разработчиков [dvmn.org](https://dvmn.org/).
