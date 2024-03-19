
from telebot.types import ReplyKeyboardMarkup , KeyboardButton


from src.bot.strings import SEND_CODE , DISABLE_NOTIFICATION ,ENABLE_NOTIFICATION

from src.bot.bot import bot

from src.bot.handlers.code import handle_send_login_code

@bot.message_handler(commands=['start'])
def start(message):
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    sendCodeBtn = KeyboardButton(SEND_CODE)
    disableNotificationBtn = KeyboardButton(DISABLE_NOTIFICATION)

    markup.add(sendCodeBtn , disableNotificationBtn)

    bot.send_message(message.from_user.id, "Select options", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_login_code(message):

    if message.text == SEND_CODE:
        handle_send_login_code(message)
        return