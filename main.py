import math
import variable as v
from telebot import *

bot = telebot.TeleBot('5163595458:AAFruP6yLGyLMCBKAg0YtEvqUu80nobUPUc')

sin = open('math_functions_value/sin').readlines()
cos = open('math_functions_value/cos').readlines()
cos.reverse()


@bot.message_handler(commands=['start'])
def start_message(message):
    start = bot.send_message(message.chat.id, v.start)
    bot.register_next_step_handler(start, next_step_log)
    bot.register_next_step_handler(start, sin_func)


@bot.message_handler(commands=['log'])
def next_step_log(message):
    msg = bot.send_message(message.chat.id, v.loginput)
    bot.register_next_step_handler(msg, log_mane_shawty_damn)


def log_mane_shawty_damn(message):
    s = message.text
    l = len(s)
    nums = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            nums.append(int(s_int))
    if len(nums) == 2:
        log = math.log(int(nums[0]), int(nums[1]))
        bot.send_message(message.chat.id, str(round(log, 3)))
    else:
        bot.send_message(message.chat.id, v.error)


@bot.message_handler(commands=['sin', 'cos', 'tg', 'ctg'])
def next_step_trigo(message):
    msg = bot.send_message(message.chat.id, v.trigoinput)
    if message.text == '/sin':
        bot.register_next_step_handler(msg, sin_func)
    if message.text == '/cos':
        bot.register_next_step_handler(msg, cos_func)
    if message.text == '/tg':
        bot.register_next_step_handler(msg, tg_func)
    if message.text == '/ctg':
        bot.register_next_step_handler(msg, ctg_func)


def sin_func(message):
    s = message.text
    l = len(s)
    nums = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            nums.append(int(s_int))
    if len(nums) == 1:
        bot.send_message(message.chat.id, sin[int(nums[0])])
    else:
        bot.send_message(message.chat.id, v.error)


def cos_func(message):
    s = message.text
    l = len(s)
    nums = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            nums.append(int(s_int))
    if len(nums) == 1:
        bot.send_message(message.chat.id, cos[int(nums[0])])
    else:
        bot.send_message(message.chat.id, v.error)


def tg_func(message):
    pass


def ctg_func(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
