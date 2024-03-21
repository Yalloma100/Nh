import telebot

BOT_TOKEN = "6754268225:AAFN5qOtXqjMemojBbY0pIHhzJWc1AH1fCI" # Замініть це своїм токеном бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Привіт, я бот, який може безкоштовно генерувати зображення. У вас 5 швидкісних генерацій та 10 повільних. Введіть команду /help щоб почати.")
bot.polling()
