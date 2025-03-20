import telebot
import random
import os
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = TeleBot(TOKEN)
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
spisok = ["/start","/hello","/bye","/help","/pass", "/calculate"]
operators = ["+","-","/","*","%","//","**","&","|","^",">>","<<"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! если ты не знаешь что написать напиши /help")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_list(message):
    bot.reply_to(message, f"вот текущий список команд: {spisok}")
    
@bot.message_handler(commands=['pass'])
def send_password(message):
    password = ""
    for i in range(10):
        password += symbols[random.randint(0,len(symbols)-1)]
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['calculate'])
def send_heh(message):
    if len(message.text.split()) == 4:
        if message.text.split()[1].isdigit() == True and message.text.split()[2] in operators and message.text.split()[3].isdigit() == True:
            first = int(message.text.split()[1])
            operator = str(message.text.split()[2])
            second = int(message.text.split()[3])
            if operator == "+":
                bot.reply_to(message, first + second)
            elif operator == "-":
                bot.reply_to(message, first - second)
            elif operator == "/":
                bot.reply_to(message, first / second)
            elif operator == "*":
                bot.reply_to(message, first * second)
            elif operator == "%":
                bot.reply_to(message, first % second)
            elif operator == "//":
                bot.reply_to(message, first // second)
            elif operator == "**":
                bot.reply_to(message, first ** second)
            elif operator == "&":
                bot.reply_to(message, first & second)
            elif operator == "|":
                bot.reply_to(message, first | second)
            elif operator == "^":
                bot.reply_to(message, first ^ second)
            elif operator == ">>":
                bot.reply_to(message, first >> second)
            elif operator == "<<":
                bot.reply_to(message, first << second)
        else:
            bot.reply_to(message, "error2")
    else:
        bot.reply_to(message, "error1")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
