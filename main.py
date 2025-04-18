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
spisok = ["/start","/EcoFact","/hello","/bye","/help","/pass 1-100 или ничего", "/calculate цифра1 оператор цифра2", "/mem 0,1 или ничего", "/bestanimal"]
operators = ["+","-","/","*","%","//","**","&","|","^",">>","<<"]
eco = ["В Тихом океане есть мусорное пятно, площадь которого достигает 1,5 млн км², что больше площади большинства стран мира. Течения сносят сюда миллионы тонн мусора ежегодно, и он превратился в подобие мусорного континента.",
"Около 12% поверхности нашей планеты имеют заповедный статус.", 
"Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.",
"Переработка отходов важна не только потому, что это экономит ресурсы, но и потому, что обычный пластик разлагается в природе более 500 лет.",
"Повышение средней мировой температуры всего на 3-4 градуса может привести к таянию льдов, глобальному наводнению и исчезновению большей части лесов на Земле.",
"Более 50% мирового урожая зерна идёт на корм скоту и на производство биотоплива.", 
"Для производства экологически чистых электромобилей используется масса вредных технологий, загрязняющих окружающую среду. В основном для производства их аккумуляторов."]
imglist = (os.listdir('images'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! если ты не знаешь что написать напиши /help")

@bot.message_handler(commands=["EcoFact"])
def send_fact(message):
    randfact = eco[random.randint(0, len(eco)-1)]
    bot.reply_to(message, f"а ты знал что {randfact}")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_list(message):
    bot.reply_to(message, f"вот текущий список команд: {spisok} а вот список всех операторов: {operators}")
    
@bot.message_handler(commands=['pass'])
def send_password(message):
    password = ""
    if len(message.text.split()) == 2:
        if message.text.split()[1].isdigit() == True:
            if int(message.text.split()[1]) >= 1 and int(message.text.split()[1]) <= 100:
                a = int(message.text.split()[1])
                for i in range(a):
                    password += symbols[random.randint(0,len(symbols)-1)]
    else:
        for i in range(10):
            password += symbols[random.randint(0,len(symbols)-1)]
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['mem'])
def send_images(message):
    if len(message.text.split()) == 2:
        if message.text.split()[1].isdigit() == True:
            a = int(message.text.split()[1])
            if a == 0 or a == 1:
                with open(f'images/{imglist[a]}', 'rb') as f:  
                    bot.send_photo(message.chat.id, f) 
    else:
        a = random.randint(0, 1)
        with open(f'images/{imglist[a]}', 'rb') as f:  
            bot.send_photo(message.chat.id, f)


def bestanimalurl():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.message_handler(commands=['bestanimal'])
def fox(message):
    image_url = bestanimalurl()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['calculate'])
def calculate(message):
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
            bot.reply_to(message, "что-то не так с содержимом")
    else:
        bot.reply_to(message, "твое сообщение слишком короткое\длинное")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
