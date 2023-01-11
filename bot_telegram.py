import telegram
import dotenv
import os

dotenv.load_dotenv('venv/.env')
token = os.getenv('BOT_TOKEN')
print(token)
bot = telegram.Bot(token=token)
print(bot.get_me())
updates = bot.get_updates()
print(updates)
chat_id = '@Astro_photos'
print(chat_id)
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
