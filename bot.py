import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from transliterate import translit
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')

    russian = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 
               'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 
               'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']
    latin = ['A', 'B', 'V', 'G', 'D', 'E', 'E', 'ZH', 'Z', 'I', 'I', 'K', 
             'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'KH', 'TS',
             'CH', 'SH', 'SHCH', 'Y', 'IE', 'E', 'IU', 'IA']
    
    name_translit = ''.join([latin[russian.index(i.upper())] if i.upper() in russian else '' for i in text])

    await bot.send_message(chat_id=user_id, text=name_translit)



if __name__ == '__main__':
    dp.run_polling(bot)