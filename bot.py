import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply(f'Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>SharlotkaTestBot</b>, бот для быстрого заказа обеда из '
                    'кафе Шарлотка.', parse_mode='html', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




