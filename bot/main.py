from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import configparser
import logging

config = configparser.ConfigParser()
config.read("settings.ini")
tokenBot = config["bot"]["bot_token"]

bot = Bot(token=tokenBot)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

# стандартная цена - 3 рубля минута
menu_buttons = ['👥 Пригласить коллег', '💳 Оплатить подписку', '👤 Профиль', '⚙️ Настройки']
subscription = ['👑 1 месяц - 43200 руб.', '👑 6 месяцев - 250 000 руб.', '👑 12 месяцев - 510 000 руб.','Выход']

def keyboards_create(ListNameBTN, NumberColumns=2):
    keyboards = types.ReplyKeyboardMarkup(
        row_width=NumberColumns, resize_keyboard=True)
    btn_names = [types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
        await message.answer(f'Добро пожаловать, {message.from_user.username}!', reply_markup=keyboards_create(menu_buttons))


@dp.message_handler(text='💳 Оплатить подписку')
async def spam_comments(message):
    await message.answer('Выберите тип подписки:', reply_markup=keyboards_create(subscription))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)