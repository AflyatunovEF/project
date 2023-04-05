import logging
import random

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Указываем токен, полученный от BotFather
TOKEN = '6245556889:AAFdWr67VccbvYIzLoesfaf3peWEjX5_pvk'

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Функция, которая выбирает одного победителя
def choose_winner(usernames):
    return random.choice(usernames)


# Хэндлер на сообщение "кто победил"
@dp.message_handler(regexp=r'кто победил ([\w-]+) или ([\w-]+)\?')
async def choose_winner_handler(message: types.Message):
    match = message.text.split()
    username1 = match[2]
    username2 = match[4]
    winner = choose_winner([username1, username2])
    text = f"Победил {winner}!"
    await message.reply(text, parse_mode=ParseMode.HTML)


# Запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
