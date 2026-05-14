import telebot
from dotenv import load_dotenv
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def send_help(message):     
    bot.send_message(message.chat.id, "Керування відбувається кнопками.")

def send_info(message): 
    bot.send_message(message.chat.id, "Це інформуючий бот, який зможе допомогти тваринам.")

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
def send_welcome(message): 
    send_info()

@bot.message_handler(commands=['help'])
def send_welcome(message): 
    send_help()

@bot.message_handler(func=lambda message: True)
def handler_message(message):
    if message.text == "Допомога": 
        bot.send_message(message.chat.id, "Допомога", reply_markup=reply_keyboard())
    elif message.text == "Інформація": 
        bot.send_message(message.chat.id, "Це інформуючий бот", reply_markup=reply_keyboard())
    elif message.text == "Бездомні тварини": 
        bot.send_message(message.chat.id, "Список буде додано пізніше", reply_markup=reply_keyboard())
    elif message.text == "Чим допомогти": 
        bot.send_message(message.chat.id, "Нічим", reply_markup=reply_keyboard())
    elif message.text == "Повідомити про тварину": 
        bot.send_message(message.chat.id, "Тут ви можете повідомити про знайдену безпритульну або пошкоджену тварину", reply_markup=reply_keyboard())
    elif message.text == "Що робити": 
        bot.send_message(message.chat.id, "Що робити, якщо ви знайшли травмовану тварину", reply_markup=reply_keyboard())
    else: 
        bot.send_message(message.chat.id, "Керування відбувається кнопками.")

bot.polling()