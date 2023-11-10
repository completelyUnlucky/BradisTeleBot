import math
import variable as v
from telebot import *

bot = telebot.TeleBot('5163595458:AAFruP6yLGyLMCBKAg0YtEvqUu80nobUPUc') # Выходи из акков и не пали ключи в паблик проектов

sin = []
cos = []
tg = []
for i in range(0, 2001):
    degree = i / 360 * 2 * math.pi
    sin.append(round(math.sin(degree), 4))
    cos.append(round(math.cos(degree), 4))
    tg.append(round(math.tan(degree), 4))


def find_numbers(message):
    serega = message.text
    lena = len(serega)
    nums = []
    igor = 0
    while igor < lena:
        s_int = ''
        a = serega[igor]
        while '0' <= a <= '9':
            s_int += a
            igor += 1
            if igor < lena:
                a = serega[igor]
            else:
                break
        igor += 1
        if s_int != '':
            nums.append(int(s_int))
    return nums


@bot.message_handler(commands=['start'])
def start_message(message):
    start = bot.send_message(message.chat.id, v.start)
    bot.register_next_step_handler(start, next_step)


@bot.message_handler(commands=['sin', 'cos', 'tg', 'log'])
def next_step(message):
    msg = bot.send_message(message.chat.id, 'Хорошо, наносекундочку...')
    if message.text == '/sin':
        bot.send_message(message.chat.id, v.trigoinput)
        bot.register_next_step_handler(msg, sin_func)
    if message.text == '/cos':
        bot.send_message(message.chat.id, v.trigoinput)
        bot.register_next_step_handler(msg, cos_func)
    if message.text == '/tg':
        bot.send_message(message.chat.id, v.trigoinput)
        bot.register_next_step_handler(msg, tg_func)
    if message.text == '/log':
        bot.send_message(message.chat.id, v.loginput)
        bot.register_next_step_handler(msg, log_mane_shawty_damn)


def log_mane_shawty_damn(message):
    if len(find_numbers(message)) == 2:
        log = math.log(int(find_numbers(message)[0]), int(find_numbers(message)[1]))
        bot.send_message(message.chat.id, str(round(log, 3)))
    else:
        bot.send_message(message.chat.id, v.error)


def sin_func(message):
    if len(find_numbers(message)) == 1:
        bot.send_message(message.chat.id, str(sin[int(find_numbers(message)[0])]))
    else:
        bot.send_message(message.chat.id, v.error)


def cos_func(message):
    if len(find_numbers(message)) == 1:
        bot.send_message(message.chat.id, str(cos[int(find_numbers(message)[0])]))
    else:
        bot.send_message(message.chat.id, v.error)


def tg_func(message):
    if len(find_numbers(message)) == 1:
        bot.send_message(message.chat.id, str(tg[int(find_numbers(message)[0])]))
    else:
        bot.send_message(message.chat.id, v.error)


if __name__ == '__main__': 
    try:
       bot.polling(none_stop=True) 
    except Exception as e:
       print(e) 
       time.sleep(15)
