import logging
import config
import time
from base.gif_source import GifSource
from base.data import UserStorage
from base.reply import BotReplyKeyboards
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
#bot = Bot(token=config.BOT_API_TOKEN, proxy=config.BOT_PROXY_URL)
bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)

# User data storage
storage = UserStorage()

# Default keyboard menu
default_keyboard = BotReplyKeyboards.default_reply()
text_render_keyboard = BotReplyKeyboards.text_render_reply()

# Start and help text message
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=config.WELCOME_TEXT, reply_markup=default_keyboard)


async def send_cats(message, count):
     if storage.data_get(message.from_user.id, 'use_file_cash') == '01' and storage.data_get(message.from_user.id, 'use_file_cash_time') + 60 < time.time():
        for url in GifSource.get_random_lines_from_file(count):
            await message.answer_document(document=url, reply_markup=default_keyboard)

     else

# 2 cats handler
@dp.message_handler(lambda message: message.text == 'Two cats')
async def multi_cats(message: types.Message):
    for i in range(2):
        url = await GifSource.get_random_cat_url()
        await message.answer_document(document=url, reply_markup=default_keyboard)


# 3 cats handler
@dp.message_handler(lambda message: message.text == 'Three cats')
async def multi_cats_big(message: types.Message):
    for i in range(3):
        url = await GifSource.get_random_cat_url()
        await message.answer_document(document=url, reply_markup=default_keyboard)


# Gif text handler
@dp.message_handler(lambda message: message.text == 'Your text')
async def text_render(message: types.Message):

    # Set step data
    storage.data_set(message.from_user.id, 'step', 'text_render')
    await bot.send_message(chat_id=message.chat.id, text=config.RENDER_TEXT, reply_markup=text_render_keyboard)


# About bot handler
@dp.message_handler(lambda message: message.text == 'About')
async def about_bot(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=config.ABOUT_TEXT, reply_markup=default_keyboard)


# Base handler
@dp.message_handler()
async def cats(message: types.Message):
    if storage.data_get(message.from_user.id, 'step') == 'text_render':

        # Render gif with text from message
        storage.data_set(message.from_user.id, 'step', '')
        await bot.send_message(chat_id=message.chat.id, text=config.RENDER_TEXT_WAIT, reply_markup=text_render_keyboard)
        await message.answer_document(document=config.RENDER_TEXT_URL.replace('{text}', message.text), reply_markup=default_keyboard)
    else:
        url = await GifSource.get_random_cat_url()
        await message.answer_document(document=url, reply_markup=default_keyboard)


# Start bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
