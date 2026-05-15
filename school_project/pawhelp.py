import telebot
from dotenv import load_dotenv
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def send_help(message):     
    bot.send_message(message.chat.id, "Керування ботом  може відбуватися декількома способами: \n▫ Reply- та Inline-кнопками \n▫Командами з  меню", reply_markup=reply_keyboard())

def send_info(message): 
    bot.send_message(message.chat.id, "Це інформуючий бот, який у якому ви можете дізнатися як допомогти організаціям з допомоги тваринам.", reply_markup=reply_keyboard())

def send_map(message): 
    keyboard = InlineKeyboardMarkup()
    go_to_map = InlineKeyboardButton("Перейти на карту", call_back="map")
    keyboard.add("Перейти на карту")
    bot.send_photo(message.chat.id, ,  reply_markup=keyboard)

def reply_keyboard(): 
    rkeyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    help = KeyboardButton("Допомога")
    info = KeyboardButton("Інформація")
    animals = KeyboardButton("Бездомні тварини")
    what_help = KeyboardButton("Чим допомогти")
    new_animal = KeyboardButton("Повідомити про тварину")
    what_to_do = KeyboardButton("Що робити")
    rkeyboard.add(help, info, animals, what_help, new_animal, what_to_do)
    return rkeyboard

load_dotenv()
bot = telebot.TeleBot(os.getenv("PAW_HELP_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, "Привіт", reply_markup=reply_keyboard())

@bot.message_handler(commands=['info'])
def send_info(message): 
    send_info()

@bot.message_handler(commands=['help'])
def send_help(message): 
    send_help()
    
@bot.message_handler(commands=['map'])
def send_map(message):
    send_map()

@bot.message_handler(func=lambda message: True)
def handler_message(message):
    if message.text == "Допомога": 
        send_help()
    elif message.text == "Інформація": 
        send_info()
    elif message.text == "Бездомні тварини": 
        bot.send_message(message.chat.id, "Список буде додано пізніше", reply_markup=reply_keyboard())
    elif message.text == "Чим допомогти": 
        bot.send_message(message.chat.id, "Поки не було додано жодної тварини.", reply_markup=reply_keyboard())
    elif message.text == "Повідомити про тварину": 
        bot.send_message(message.chat.id, "Тут ви можете повідомити про знайдену безпритульну або пошкоджену тварину", reply_markup=reply_keyboard())
    elif message.text == "Що робити": 
        bot.send_message(message.chat.id, "Якщо ви знайшшли травмовану, або безпритульну тварину,  ви можете звернутися до:\nВетеринарної клініки: \n*** \nПритулку: \n«Кременчуцькі Хвостики»«КП "Спецсервіс-Кременчук"»: +380 (67) 203 21 97" \
                        "\n▫«Кременчуцькі Хвостики»: +380 (97) 287 75 44", 
                         reply_markup=reply_keyboard())
    else: 
        send_help()

bot.polling()
