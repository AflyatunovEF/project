import random
import time
import logging
from aiogram import Bot, Dispatcher, types, executor

# Укажите токен вашего бота
TOKEN = '5744863972:AAE-JeYBvzxgy1hE4IxB2HWAmFQXG_LNBDM'

# Инициализируйте бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Создайте функцию, которая будет выбирать случайного участника из списка
def choose_winner(participants):
    return random.choice(participants)


# Добавьте обработчик команды /winner
@dp.message_handler(commands=['winner'])
async def choose_random_winner(message: types.Message):
    # Получите список участников чата
    chat_id = message.chat.id
    participants = []
    async for member in bot.iter_chat_members(chat_id=chat_id):
        if not member.user.is_bot:
            participants.append(member.user.username)
    # Выберите победителя
    winner = choose_winner(participants)
    # Отправьте сообщение с победителем
    await message.answer(f"Победитель выбран: @{winner}")


# Запустите бота
if __name__ == '__main__':
    executor.start_polling(dp)

PROXY_URL = "http://proxy.server:3128"
bot = Bot(proxy=PROXY_URL)
