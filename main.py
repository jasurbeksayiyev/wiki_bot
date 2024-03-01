
import logging
import  wikipedia

import wikipedia
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '7077374391:AAGVAGHQrjRibm17oygOB9tjxC7j06RASEk'

wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(" Assalomu Aleykum! Botimizga Xush kelibsiz!  ")



@dp.message_handler()
async def sentWiki(message: types.Message):
   try:
        respond = wikipedia.summary(message.text)
        await  message.answer(respond)
   except:
         await message.answer("Bu tema boyicha hichnma yo manda Jasur akadan sorang sizga yordam beradi")

if __name__ == '__main__':
    executor.start_polling(dp,  skip_updates=True