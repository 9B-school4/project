import telebot
from telebit.type import KeyboardMarkup, ReplykeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def send_help(message): 
  bot.send_message(message.chat.id, "Керування відбувається кнопками.")

def send_info(message): 
  bot.send_message(message.chat.id, "Це інформуючий бот, який зможе допомогти тваринам.")

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def send_welcome(message): 
  rkeyboard = KeyboardMarkup(resize=4)
  help = ReplyKeyboardButton("Допомога")
  info = ReplyKeyboardButton("Інформація")
  animals = ReplyKeyboardButton("Бездомні тварини")
  what_help = ReplyKeyboardButton("Чим допомогти")
  new_animal = ReplyKeyboardButton("Повідомити про тварину")
  what_to_do = ReplyKeyboardButton("Що робити")
  rkeyboard.add(help, info, animals, what_help, new_animal, what_to_do)
  bot.send_message(message.chat.id, "Привіт")