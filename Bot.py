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


numbon = 0
illo = 0
keys = ["sk-UIZeQsYPmIQ0lwmh3O0Gd6MpXhsAUlddr7D44F7gsDROrWj0","sk-5gFDGrO5BlG0czCBySy7bEKqd6V5vVs5lgNWD3OfK0smjIGf","sk-OXEHIC5WhhAhzDzpaFjDxD0j64V0nFA6ZX1yhvarS4Jblo2J","sk-4y5i5B53VRs9jV4gMc86X8vtUQu3LaIlhIii1GFJFFAvjzkE","sk-mDwdWJG4KEiMHZioSPJtqR36gkRAtaIBHYOfVgmtl3IqGGGJ","sk-GWLEuuG9bkwMetggsuxQvZWwgxDvBWWMsJYZF9pr2SVZ4iep","sk-9WBACQuRibyvYFTlKqEKBdglNd4Ti0dzbxy99u6SHvK4pdjW","sk-PYHffx0JIe2EM75GH2zax6mU5RYb3uz9bjCLdMa86Rbh1PiY","sk-gy3ufunqVTF6TVssRpYjUyop3N0phIBrreGBnt8oEANiW9Dt","sk-INTOAi19LNZ3lpLoIfudOuH5rrct3vsOuKaqExQDnW9H1VoZ","sk-FVlWPqufhMgRN3WzTZoCXKi4IybQrOrIv9YLqX8CMBCoT7lM","sk-WgdoQyjywKeNK1pRQf02FT7AdxqsJiYOGiq3cQn5WxwBvOX2","sk-QCVQ0PVYCbXwEsvGCDqxpjovpBNrHCX3aa8ZPpN2esKTYWue","sk-HLf4j5gLaFDbKRsCAhs0EZT1XZxzJcJJAXgWfoOZe0Byrk0B","sk-t9buh9V5u0lhaWyiugJBRltcEYJnjWZHh9129plouJBwOViQ","sk-nPQfH9RsXvylgwGPH1utUoDfmdJ3xuW7vf9G5n9q3x3VMnHk","sk-1a0qO9YN0EMoIHqS943Z5X2qooyIM3ztqtaFN1oVzQNJzJYX","sk-7wBFp3o5bkfvOXmQDDBo18iXDLtfFplVEplsFUsLvS3tKOe2","sk-9S3eJoU78CwPW74BBaSeJzmeZf9QOEHmCKLSGvXoOcV2u6KK","sk-8aEWXvsOeIUmTZXDO6vzKl6lllbQc6De2iAxPoQyw1M7BCLG","sk-3jEtVIxy83PZdYCcg4eYOVO3ide53A7KJQDYWpHSebW6YDnl","sk-PBhcupWfxvs6gEUZz77wKnpXmrJ7gXvAton47CqCh3GaiMwd","sk-sXIgnZh5TZoQ8U0QKTNNfboXL3Vq3zwtFgTCUFGC5CIq2rvI","sk-LivdKXpYUX24ig48kaY0ZL3RYa54TOlSpp7LQPWZxxn21OzS","sk-5AFzY3keaHV8RaauJbZGunlCdeLT295Z0subZNpz0o0fD0e3"]
keycode = "sk-e30dLmY0paQJJavLUaJuvt0NRvKlFhC64YON14cL8jDnucqF"


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
        generations[user_id] = 5
        quick_generations[user_id] = 2



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
    generations[user_id] = 5
    quick_generations[user_id] = 2




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
      generations[user_id] = 5

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
          global keycode
          global illo
          global numbon
          illo+=1
          if illo == 8:
              numbon+=1
              keycode = keys[numbon]
              illo = 0
              print("keycode:", keycode)

          response = requests.post(
          f"https://api.stability.ai/v2beta/stable-image/generate/core",
          headers={
              "authorization": keycode,
              "accept": "image/*"
          },
          files={
              "none": ''
          },
          data={
              "prompt": prompt,
              "output_format": "webp",
          },
      )

          if response.status_code == 200:
              with open("./lighthouse.webp", 'wb') as file:
                  file.write(response.content)
          else:
              raise Exception(str(response.json()))
          url = open('./lighthouse.webp', 'rb')
     # Видаліть останнє повідомлення, яке ваш бот відправив у чат користувача
          bot.send_photo(message.chat.id, url, caption=f"💬Промт:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** повільних генерацій.", parse_mode="Markdown")
          generations[user_id] -= 1
   except:
     bot.send_message(message.chat.id, "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport.")
  # Зменшення кількості генерацій





def bumon2 (message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in quick_generations:
    quick_generations[user_id] = 2

  if quick_generations[user_id] <= 0:
      bot.send_message(message.chat.id, "Ви вже використали всі генерації на день.")
      return
  bot.send_message(message.chat.id, "💨Почалась швидка генерація, зазвичай вона триває до 2 хвилин")

  # Генерація зображення
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')

  prompt = resut

# Output: Bu bir örnektir.
  try:
        time.sleep(35)
        global keycode
        global illo
        global numbon
        illo+=1
        if illo == 8:
            numbon+=1
            keycode = keys[numbon]
            illo = 0
            print("keycode:", keycode)

        response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": keycode,
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": prompt,
            "output_format": "webp",
        },
    )

        if response.status_code == 200:
            with open("./lighthouse.webp", 'wb') as file:
                file.write(response.content)
        else:
            raise Exception(str(response.json()))
        url = open('./lighthouse.webp', 'rb')
        bot.send_photo(message.chat.id, url, caption=f"💬Промт:` {prompt}\n`\n💰У вас залишилося ***{quick_generations[user_id] - 1}*** швидких генерацій.", parse_mode="Markdown")
        quick_generations[user_id] -= 1
  except:
                  bot.send_message(message.chat.id, "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport.")





def help(message):
  bot.send_message(message.chat.id, "Я RubiGen, можу генерувати зображення по їх опису.\n\nПідпишіться на Канал RubiGen: @RubiGenChanel.\nЧат RubiGen: @RubiGenChat - Там роздають промокоди на генерацію зображень.\n\nКоманди:\n/buy - ❤Купити Premium підписку на бота RubiGen❤\n/gen - Генерувати зображення.\n/help - Допомога та команди.\n/balance - Перевірити баланс.\n/promo - Ввести промокод.\n/promter - (BETA) Покращиити промт за допомогою PROmter.\n\nЗа іншими питаннями звертайтесь до адміна: @RubiGenSupport.\n")

# Функція для обробки команди перевірки залишку генерацій
def check_generations(message):
    user_id = message.from_user.id

    # Перевірка наявності користувача
    if user_id not in generations:
        generations[user_id] = 5
        quick_generations[user_id] = 2

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









@bot.message_handler(commands=['add'])
def add_api_key(message):
  if message.chat.id == 6133407632:
    global keys
    bot.send_message(message.chat.id, "Введіть ключ:")
    bot.register_next_step_handler(message, add_key)
  else:
    return

def add_key(message):
    global numbon
    global keys
    key = message.text
    keys.append(key)
    bot.send_message(message.chat.id, f"Ключ додано.\n\nУ вас залишилось {numbon} працюючих ключів\n\n\nКлючі:\n" + "\n".join(keys))





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
    generations[user_id] = 5
    quick_generations[user_id] = 2

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
       bot.reply_to(message, "Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас 2 швидкісних генерацій та 5 повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
    elif user_d not in all_users:
        # Запис ID користувача в файл
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

        # Додавання ID користувача до списку
        all_users.append(user_id)
        bot.reply_to(message, "Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас 2 швидкісних генерацій та 5 повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
    # Створення запису для нового користувача
    if user_id not in generations:
        generations[user_id] = 5
        quick_generations[user_id] = 2






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

