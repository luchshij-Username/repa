import telebot
import random
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("твой токен")
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
spisok = ["/start","/hello","/bye","/help","/pass"]

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

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
