from telebot.types import InlineKeyboardMarkup , InlineKeyboardButton

from src.bot.bot import bot
from src.db.models.code import update_login_code
from src.config import CODE_LENGTH , CODE_ADDED_NUMBERS , CODE_LIFE_TIME , BASE_URL

import random
import string 

from datetime import timedelta
import humanize


def handle_send_login_code(message):

    code = generat_code()

    lifeTime = timedelta(seconds=CODE_LIFE_TIME)

    update_login_code(str(message.from_user.id) , code)

    markup = InlineKeyboardMarkup()
    copyBtn = InlineKeyboardButton(text='Use code' ,  url=f'{BASE_URL}?code={code}')
    markup.add(copyBtn)

    bot.send_message(message.from_user.id, f"Your login code: {code}\nCode is valid for: {humanize.naturaldelta(lifeTime)}", reply_markup = markup)



def generat_code() -> str: 

    letters = string.ascii_uppercase
    numbers = "123456789"

    chars =  [ random.choice(letters) for _ in range(CODE_LENGTH)] + [ random.choice(numbers) for _ in range(CODE_ADDED_NUMBERS)]

    return ''.join(chars)