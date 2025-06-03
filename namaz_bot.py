import telebot

TOKEN = 'сюда_вставь_токен_от_BotFather'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ассаляму алейкум! Это NamazBot.")

bot.polling()
