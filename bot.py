import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply('Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для быстрого заказа обеда из '
                    'кафе Шарлотка. '.format(message.from_user, bot.get_me()), parse_mode='html')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




