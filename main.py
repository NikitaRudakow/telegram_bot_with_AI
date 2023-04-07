from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from gpt import generate_response
import logging

logger = logging.getLogger(__name__)

TOKEN = "5942337165:AAH7DltbrcIzFk5mvj4B7g-rJXnrOkazRM0"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(msg: types.Message):
#     await msg.reply_to_message(f"Я бот. Приятно познакомиться,{msg.from_user.first_name}")

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    try:
        response = await generate_response(msg.text)
        print(f"New message: {msg.text}\nanswer: {response}\n\n")
        await msg.answer(response)
    except:
        await msg.answer("Извините, бот временно недоступен(\nНо скоро это изменится")


if __name__ == '__main__':
   executor.start_polling(dp)