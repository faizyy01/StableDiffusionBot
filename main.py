import logging
from dotenv import load_dotenv
import os 
import requests
import time
load_dotenv() 
import base64
import io

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")
APIKEY = os.getenv("APIKEY")

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

# def poll(task_id):
#     res = requests.get(f'{URL}/sb/task/{task_id}')
#     data = res.json()
#     print(data)
#     if(data.get('task_status') == "SUCCESS"):
#         url = data.get('task_result')
#         print(f'{url}')
#         return f'{url}'
#     if(data.get('task_status') == "FAILED"):
#         return "Error"
#     time.sleep(3)
#     return poll(task_id)

def image(update, context):
    print(update.message.text.replace('/image ', ''))
    msg = update.message.reply_text('https://i.pinimg.com/originals/2c/bb/5e/2cbb5e95b97aa2b496f6eaec84b9240d.gif')
    payload = {'prompt':update.message.text.replace('/getImage', ''), 'format': 'jpeg', 'num_images': "1"
    ,'guidance_scale': "7.5", 'num_inference_steps': "50", 'num_images': "1", 'height': "512", 'width': "512", 'use_ldm': "false"}

    headers = {'X-API-Key': APIKEY}
    res = requests.get(f'{URL}/txt2img', params=payload, headers=headers, stream = True)
    res.raw.decode_content = True
    # im = Image.open(res.raw)
    # print(im.format, im.mode, im.size)
    # data = res.json()
    # print(data.get('task_id'))
    # url = poll(data.get('task_id'))
    update.message.bot.send_photo(update.message.chat.id, photo=res.raw)
    #update.message.bot.deleteMessage(update.message.chat_id, )

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, image))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    main()