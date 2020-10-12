import config
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
admin = config.ADMIN
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
today_menu_button = types.KeyboardButton('Сегодня в меню')
start_order_button = types.KeyboardButton('Заказать обед')


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply('Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для '
                        'быстрого заказа обеда из кафе Шарлотка.'
                        .format(message.from_user, await bot.get_me()), parse_mode='html', reply_markup=markup)


@dp.message_handler(commands='edit')
async def edit_menu(message):
    if message.chat.username == admin:
        await bot.send_message(message.chat.id, 'Поздравляю, вы админ')
    else:
        await bot.send_message(message.chat.id, 'У вас нет прав на данное действие')


@dp.message_handler(content_types='text')
async def buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Сегодня в меню':
            await bot.send_message(message.chat.id, 'В разработке')
        elif message.text == 'Заказать обед':
            await bot.send_message(message.chat.id, 'Тоже в разработке')
        else:
            await bot.send_message(message.chat.id, 'Нажмите одну из кнопок')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
