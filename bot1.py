import random
from aiogram import Bot, Dispatcher, types, executor

# Токен бота, который нужно получить у BotFather в Telegram
BOT_TOKEN = '6068004483:AAHdAyF_dn0b4-TSgmNRrAi0vao0m9mgFK0'

# Создаем объект бота
bot = Bot(token=BOT_TOKEN)

# Создаем объект dispatcher и передаем ему объект бота
dp = Dispatcher(bot)

# Список участников чата
chat_users = []

# Хэндлер на команду /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply('Привет! Я буду рандомно выбирать победителя среди участников чата.')

# Хэндлер на команду /add_user
@dp.message_handler(commands=['add_user'])
async def add_user(message: types.Message):
    # Добавляем пользователя в список, если его там еще нет
    if message.from_user not in chat_users:
        chat_users.append(message.from_user)
        await message.reply(f'Пользователь {message.from_user.full_name} добавлен.')
    else:
        await message.reply('Вы уже добавлены в список участников.')

# Хэндлер на команду /choose_winner
@dp.message_handler(commands=['choose_winner'])
async def choose_winner(message: types.Message):
    # Если в списке участников есть хотя бы один пользователь
    if chat_users:
        # Рандомно выбираем победителя из списка участников
        winner = random.choice(chat_users)
        # Отправляем сообщение с ником победителя
        await message.reply(f'Победитель: {winner.username}!')
    else:
        await message.reply('В списке участников пока нет ни одного пользователя.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
