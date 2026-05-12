import telebot

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def send_welcome(message): 
  bot.send_message(message.chat.id, "Привіт")
