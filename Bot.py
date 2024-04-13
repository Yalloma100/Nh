import os
import requests
import telebot
import time
from background import keep_alive
from telebot import types

BOT_TOKEN = "6754268225:AAFN5qOtXqjMemojBbY0pIHhzJWc1AH1fCI" # Замініть це своїм токеном бота
bot = telebot.TeleBot(BOT_TOKEN)

phone_number = None
myid = [6133407632]

startuser = []
addpromocodesss = ""
usernameid = ""

# Створення словника для зберігання інформації про генерації
generations = {}
quick_generations = {}
@bot.message_handler(commands=['gen'])
# Функція для обробки команди генерації зображення
def generate_image(message):
    user_id = message.from_user.id
    user_d = message.chat.id
    # Створення двох кнопок
    button_1 = types.KeyboardButton("Повільна генерація")
    button_2 = types.KeyboardButton("Швидка генерація")

    # Створення клавіатури з двома рядами
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(button_1, button_2)

    # Відправлення повідомлення з двома кнопками
    if user_id in all_users:
      bot.send_message(message.chat.id, "Виберіть яку генерацію ви хочете використати👇", reply_markup=keyboard)
    elif user_d not in all_users:
        # Запис ID користувача в файл
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

        # Додавання ID користувача до списку
        all_users.append(user_id)
        bot.send_message(message.chat.id, "Виберіть яку генерацію ви хочете використати👇", reply_markup=keyboard)
    # Створення запису для нового користувача
    if user_id not in generations:
        generations[user_id] = 10
        quick_generations[user_id] = 5



@bot.message_handler(commands=["promo"])
def promo_handr(message):
    user_id = message.chat.id
    try:
    # Отримання тексту повідомлення
      text = message.text.split(' ')[1]
    except:
      bot.send_message(message.chat.id, "Вводьте в такому форматі: \n/promo code, на місті \"code\" вставте ваш промокод.")
      return
    # Перевірка, чи вже користувач активував промокод
    if text in activated_promocodes.get(user_id, []):
        bot.send_message(message.chat.id, "Ви вже активували промокод.")
        return

    # Перевірка, чи введений промокод дійсний
    if text not in promocodes:
        bot.send_message(message.chat.id, "Неправильний промокод.")
        return

    # Активація промокоду
    activated_promocodes.setdefault(user_id, []).append(text)
    bot.send_message(message.chat.id, "Промокод активовано!")
    generations[user_id] = 10
    quick_generations[user_id] = 5




# Функція для обробки натискань на кнопки
@bot.message_handler(func=lambda message: message.text in ["Швидка генерація", "Повільна генерація"])
def handle_buttons(message):
    user_id = message.from_user.id
    user_d = message.chat.id
    if user_id in all_users:
      if message.text == "Швидка генерація":
          # Створення клавіатури для видалення
          keyboard_remove = types.ReplyKeyboardRemove()
          bot.send_message(message.chat.id, "Введіть промт для генерації👇", reply_markup=keyboard_remove)
          bot.register_next_step_handler(message, bumon2)
      elif message.text == "Повільна генерація":
        # Створення клавіатури для видалення
        keyboard_remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введіть промт для генерації👇", reply_markup=keyboard_remove)
        bot.register_next_step_handler(message, bumon1)
    elif user_d not in all_users:
    # Запис ID користувача в файл
      with open("users.txt", "a") as f:
        f.write(f"{user_id}\n")
    # Додавання ID користувача до списку
      all_users.append(user_id)
      handle_buttons(message)


def bumon1 (message):
   prompt = message.text
   user_id = message.from_user.id
  # Перевірка залишку генерацій
   if user_id not in generations:
      generations[user_id] = 10

   if generations[user_id] <= 0:
      bot.send_message(message.chat.id, "Ви вже використали всі генерації на день.")
      return
   bot.send_message(message.chat.id, "💤Почалась повільна генерація, зазвичай вона триває до 5 хвилин")
   user_id = message.chat.id
   from easygoogletranslate import EasyGoogleTranslate
   translator = EasyGoogleTranslate()
   resut = translator.translate(prompt, target_language='en')
   prompt = resut
   try:
     time.sleep(100)
     from gradio_client import Client

     client = Client("AP123/Playground-v2.5")
     result = client.predict(
         prompt,	# str  in 'Enter your image prompt' Textbox component
         50,	# float (numeric value between 1 and 75) in 'Number of Inference Steps' Slider component
         5,	# float (numeric value between 1 and 10) in 'Guidance Scale' Slider component
         api_name="/generate_image"
     )
     url = "https://ap123-playground-v2-5.hf.space/file=" + result
     # Видаліть останнє повідомлення, яке ваш бот відправив у чат користувача
     time.sleep(5)
     bot.send_photo(message.chat.id, url, caption=f"💬Промт:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** повільних генерацій.", parse_mode="Markdown")
     generations[user_id] -= 1
   except:
     bot.send_message(message.chat.id, "Помилка генерації зображення, спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport.")
  # Зменшення кількості генерацій





def bumon2 (message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in quick_generations:
    quick_generations[user_id] = 5

  if quick_generations[user_id] <= 0:
      bot.send_message(message.chat.id, "Ви вже використали всі генерації на день.")
      return
  bot.send_message(message.chat.id, "💨Почалась швидка генерація, зазвичай вона триває до 2 хвилин")
  # Зменшення кількості генерацій
  quick_generations[user_id] -= 1

  # Генерація зображення
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')

  prompt = resut

# Output: Bu bir örnektir.
  try:
    time.sleep(30)
    from gradio_client import Client

    client = Client("AP123/Playground-v2.5")
    result = client.predict(
        prompt,	# str  in 'Enter your image prompt' Textbox component
        50,	# float (numeric value between 1 and 75) in 'Number of Inference Steps' Slider component
        5,	# float (numeric value between 1 and 10) in 'Guidance Scale' Slider component
        api_name="/generate_image"
    )
    url = "https://ap123-playground-v2-5.hf.space/file=" + result
    time.sleep(5)
    bot.send_photo(message.chat.id, url, caption=f"💬Промт:` {prompt}\n`\n💰У вас залишилося ***{quick_generations[user_id]}*** швидких генерацій.", parse_mode="Markdown")
  except:
                  bot.send_message(message.chat.id, "Помилка генерації зображення, спробуйте ще раз.\n\nЯкщо помилка повторилась 2 рази, зверніться до адміна: @RubiGenSupport.")





def help(message):
  bot.send_message(message.chat.id, "Я RubiGen, можу генерувати зображення по їх опису.\n\nПідпишіться на Канал RubiGen: @RubiGenChanel.\nЧат RubiGen: @RubiGenChat - Там роздають промокоди на генерацію зображень.\n\nКоманди:\n/buy - ❤Купити Premium підписку на бота RubiGen❤\n/gen - Генерувати зображення.\n/help - Допомога та команди.\n/balance - Перевірити баланс.\n/promo - Ввести промокод.\n/promter - (BETA) Покращиити промт за допомогою PROmter. \n\nЧасті запитання:\n\nЧому RubiGen не розуміє що я хочу намалювати?\nВідповідь: Промт потрібно писати англійською та більше деталізувати зображення.\n\nЧому бот повертає повністю чорне зображення?\nВідповідь: Тому що зображення порушує фільтр безпеки NSFW.\n\nЗа іншими питаннями звертайтесь до адміна: @RubiGenSupport.\n")

# Функція для обробки команди перевірки залишку генерацій
def check_generations(message):
    user_id = message.from_user.id

    # Перевірка наявності користувача
    if user_id not in generations:
        generations[user_id] = 10
        quick_generations[user_id] = 5

    # Повідомлення про залишок генерацій
    bot.send_message(message.chat.id, f"💰Наразі у вас на балансі:\n\n💨Швидких генерацій: ***{quick_generations[user_id]}***\n💤Повільних генерацій: ***{generations[user_id]}***", parse_mode="Markdown")

# Реєстрація команд
bot.register_message_handler(check_generations, commands=['balance'])
bot.register_message_handler(help, commands=['help'])

all_users = []


@bot.message_handler(commands=['send'])
def send_m(message):
  if message.chat.id == 6133407632:
    bot.send_message(message.chat.id, "Введіть повідомлення для розсилки:")
    bot.register_next_step_handler(message, send_message_to_users)
  else:
    bot.send_message(message.chat.id, "Error: you not admin")
def send_message_to_users(message):
    message_text = message.text

    with open("users.txt", "r") as f:
        for user_id in f.readlines():
            bot.send_message(user_id, message_text)











# Змінна для зберігання промокодів
promocodes = []

# Словник для зберігання активованих промокодів
activated_promocodes = {}

@bot.message_handler(commands=["promo"])
def promo_handler(message: types.Message):
  global userbuyid
  if userbuyid in usertelegids:
    bot.send_message(message.chat.id, "Ви не можите активувати ніякі промокоди.")
    user_id = message.chat.id
    try:
    # Отримання тексту повідомлення
      text = message.text.split(' ')[1]
    except:
      bot.send_message(message.chat.id, "Вводьте в такому форматі: \n/promo code, на місті \"code\" вставте ваш промокод.")
      return
    # Перевірка, чи вже користувач активував промокод
    if text in activated_promocodes.get(user_id, []):
        bot.send_message(message.chat.id, "Ви вже активували промокод.")
        return

    # Перевірка, чи введений промокод дійсний
    if text not in promocodes:
        bot.send_message(message.chat.id, "Неправильний промокод.")
        return

    # Активація промокоду
    activated_promocodes.setdefault(user_id, []).append(text)
    bot.send_message(message.chat.id, "Промокод активовано!")
    generations[user_id] = 10
    quick_generations[user_id] = 5

    # Додайте код для виконання дії після активації промокоду,
    # наприклад, надання знижки, доступу до контенту тощо.
# Функція для обробки команди start




addpromocodesss = ""


@bot.message_handler(commands=['addpromo'])
def naigfd(message):
  if message.chat.id == 6133407632:
    bot.send_message(message.chat.id, "Введіть новий промокод:")
    bot.register_next_step_handler(message, send_messall)
  else:
    bot.send_message(message.chat.id, "Error: you not admin")
def send_messall(message):
  global addpromocodesss
  addpromocodesss = message.text
  bot.send_message(message.chat.id, "Промокод додано")
  promocodes.append(addpromocodesss)






userbuyid = ""
usertelegids = []

@bot.message_handler(commands=['buy'])
def add_buy_user(message):
    global usertelegids
    user_id = message.from_user.id
    user_d = message.chat.id
    if user_d == 6133407632:
      bot.send_message(message.chat.id, "Введіть телеграм id нового premium користувача:")
      bot.register_next_step_handler(message, next_add_buy)
    else:
      global usertelegids
      global userbuyid
      if userbuyid in usertelegids:
        user_id = message.chat.id
        global generations
        global quick_generations
        generations[user_id] = 400
        quick_generations[user_id] = 200
        usertelegids.remove(userbuyid)
        bot.send_message(message.chat.id, f"<b>Вам на баланс начислено {quick_generations[user_id]} швидких генерацій та {generations[user_id]} повільних генерацій.</b>\n\n\n❗❗❗УВАГА❗❗❗\n\n❌НЕ ВИКОРИСТОВУЙТЕ КОМАНДУ \"promo\" ВИ МОЖЕТЕ ВТРАТИТИ СВОЮ Premium ПІДПИСКУ❌\n\n♥️Дякуємо що користуєтесь нашим телеграм ботом♥️", parse_mode="HTML")
      else:
        bot.send_message(message.chat.id, f"Premium підписка RubiGen Basic - Включає в себе 200 швидких генерацій, 400 повільних та велику нашу подяку.\n\nЩоб купити Premium підписку на нашого бота вам потрібно перевести 100грн на номер картки: `5375414122338071`\nЗ ось таким описом: `Оплата за Premium Basic: {message.chat.id}`\n\nПісля здійснення оплати вам прийде повідомлення про нарахування генерацій.\n\nЯкщо ви через 24 години ви не отримали одобрення платежу тоді зверніться до адміна: @RubiGenSupport.", parse_mode="Markdown")

def next_add_buy (message):
  global usertelegids
  global userbuyid
  userbuyid = message.text
  usertelegids.append(userbuyid)
  bot.send_message(message.chat.id, "Користувача додано до списку.")
  try:
    bot.send_message(userbuyid, "Вам підтвердили оплату premium підписки.\n\n❗❗❗УВАГА❗❗❗\n\n💬ВВЕДІТЬ КОМАНДУ /buy ЩОБ ОТРИМАТИ: 200 ШВИДКИХ ТА 400 ПОВІЛЬНИХ ГЕНЕРАЦІЙ💬\n\n♥️Дякуємо що користуєтесь нашим телеграм ботом♥️")
  except:
    bot.send_message(message.chat.id, f"Користувача з таким id: `{userbuyid}`, немає або користувач НЕ запустив бота.", parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_d = message.chat.id
    # Перевірка наявності ID користувача в списку
    # Очистка списку all_users
    # Перевірка наявності ID користувача в списку
    if user_id in all_users:
       bot.reply_to(message, "Привіт, я бот, який може безкоштовно генерувати зображення. У вас 5 швидкісних генерацій та 10 повільних. Введіть команду /help щоб почати.")
    elif user_d not in all_users:
        # Запис ID користувача в файл
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

        # Додавання ID користувача до списку
        all_users.append(user_id)
        bot.reply_to(message, "Вітаємо вас у RubiGen bot який може безкоштовно генерувати зображення.\nУ вас 5 швидкісних генерацій та 10 повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
    # Створення запису для нового користувача
    if user_id not in generations:
        generations[user_id] = 10
        quick_generations[user_id] = 5






    # Додайте код для виконання дії після активації промокоду,
    # наприклад, надання знижки, доступу до контенту тощо.
# Функція для обробки команди start



@bot.message_handler(commands=['promter'])
def beta_promter(message):
  bot.send_message(message.chat.id, "‼Увага‼\nНаразі ***PROmter*** це ***BETA*** версія, іноді може давати неправильні результати!\n\nВведіть ваш промт будь якою мовою, а я спробую його покращити👇", parse_mode="Markdown")
  bot.register_next_step_handler(message, promter)
def promter(message):
  chat_text = message.text
  bot.send_message(message.chat.id, "PROmter зараз займається покращенням вашого промту, зазвичай це триває до 35 секунд.")
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(chat_text, target_language='en')

  chat_text = resut
  from gradio_client import Client
  client = Client("Qwen/Qwen1.5-32B-Chat-demo")
  result = client.predict(
   query=chat_text,
   history=[],
   system="Enhance the prompt provided by the user for generating images, adding more details and improving it. Return only the improved prompt without any unnecessary words or punctuation marks.",
   api_name="/model_chat"
  )

  # Виводити лише друге значення (репліку асистента)
  writed_prompt = result[1][0][1]
  bot.send_message(message.chat.id, f"\****Покращанний промт***: `{writed_prompt}`\n\n\* - іноді PROmter може навпаки, погіршити промт.\n\n\nПриєднайтесь до каналу RubiGen щоб бачити більше новин про оновлення: https://t.me/RubiGenChanel", parse_mode="Markdown")


keep_alive()




while True:
  try:
      bot.polling(none_stop=True)
  except Exception as e:
          bot.send_message(6133407632 ,f"Помилка: {e}")
          time.sleep(1)

