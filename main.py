import variable as v
from telebot import *

bot = telebot.TeleBot('5163595458:AAFruP6yLGyLMCBKAg0YtEvqUu80nobUPUc')

keyboard = types.InlineKeyboardMarkup()
key_sinus = types.InlineKeyboardButton(text='синус', callback_data='sinus')
key_cosine = types.InlineKeyboardButton(text='косинус', callback_data='cosine')
keyboard.add(key_sinus, key_cosine)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, v.start)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, v.get_help, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, v.idk)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "синус":
        bot.send_message(call.message.chat.id, 'пока не заполнено')
    elif call.data == "косинус":
        bot.send_message(call.message.chat.id, 'пока не заполнено')


bot.polling(none_stop=True, interval=0)
