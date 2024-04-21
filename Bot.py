import os
import requests
import telebot
import time

from telebot.util import quick_markup
from background import keep_alive
from telebot import types

BOT_TOKEN = "6754268225:AAFN5qOtXqjMemojBbY0pIHhzJWc1AH1fCI" # Замініть це своїм токеном бота
bot = telebot.TeleBot(BOT_TOKEN)



quick_genaratus = 2
genaratus = 5
phone_number = None
myid = [6133407632]
numbon = 0
illo = 0
keys = ["sk-ZgidcvpxBVa55uaIpKunOt13YXNFw6q2jnpbKRFlZUwyNbB6","sk-5gFDGrO5BlG0czCBySy7bEKqd6V5vVs5lgNWD3OfK0smjIGf","sk-OXEHIC5WhhAhzDzpaFjDxD0j64V0nFA6ZX1yhvarS4Jblo2J","sk-4y5i5B53VRs9jV4gMc86X8vtUQu3LaIlhIii1GFJFFAvjzkE","sk-mDwdWJG4KEiMHZioSPJtqR36gkRAtaIBHYOfVgmtl3IqGGGJ","sk-GWLEuuG9bkwMetggsuxQvZWwgxDvBWWMsJYZF9pr2SVZ4iep","sk-9WBACQuRibyvYFTlKqEKBdglNd4Ti0dzbxy99u6SHvK4pdjW","sk-PYHffx0JIe2EM75GH2zax6mU5RYb3uz9bjCLdMa86Rbh1PiY","sk-gy3ufunqVTF6TVssRpYjUyop3N0phIBrreGBnt8oEANiW9Dt","sk-INTOAi19LNZ3lpLoIfudOuH5rrct3vsOuKaqExQDnW9H1VoZ","sk-FVlWPqufhMgRN3WzTZoCXKi4IybQrOrIv9YLqX8CMBCoT7lM","sk-WgdoQyjywKeNK1pRQf02FT7AdxqsJiYOGiq3cQn5WxwBvOX2","sk-QCVQ0PVYCbXwEsvGCDqxpjovpBNrHCX3aa8ZPpN2esKTYWue","sk-HLf4j5gLaFDbKRsCAhs0EZT1XZxzJcJJAXgWfoOZe0Byrk0B","sk-t9buh9V5u0lhaWyiugJBRltcEYJnjWZHh9129plouJBwOViQ","sk-nPQfH9RsXvylgwGPH1utUoDfmdJ3xuW7vf9G5n9q3x3VMnHk","sk-1a0qO9YN0EMoIHqS943Z5X2qooyIM3ztqtaFN1oVzQNJzJYX","sk-7wBFp3o5bkfvOXmQDDBo18iXDLtfFplVEplsFUsLvS3tKOe2","sk-9S3eJoU78CwPW74BBaSeJzmeZf9QOEHmCKLSGvXoOcV2u6KK","sk-8aEWXvsOeIUmTZXDO6vzKl6lllbQc6De2iAxPoQyw1M7BCLG","sk-3jEtVIxy83PZdYCcg4eYOVO3ide53A7KJQDYWpHSebW6YDnl","sk-PBhcupWfxvs6gEUZz77wKnpXmrJ7gXvAton47CqCh3GaiMwd","sk-sXIgnZh5TZoQ8U0QKTNNfboXL3Vq3zwtFgTCUFGC5CIq2rvI","sk-LivdKXpYUX24ig48kaY0ZL3RYa54TOlSpp7LQPWZxxn21OzS","sk-5AFzY3keaHV8RaauJbZGunlCdeLT295Z0subZNpz0o0fD0e3"]
keycode = "sk-mNRJtuyJfNut85dZCptVBgYqn4SoPHYtJ1Hp6WpuGrKizOLR"
startuser = []
addpromocodesss = ""
usernameid = ""


# Створення словника для зберігання інформації про генерації
generations = {}
quick_generations = {}
@bot.message_handler(commands=['gen'])
# Функція для обробки команди генерації зображення
def generate_image(message):
    global quick_genaratus
    global genaratus
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
        generations[user_id] = genaratus
        quick_generations[user_id] = quick_genaratus



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
      generations[user_id] = genaratus
   genenenenenenra = int(generations[user_id])
   if genenenenenenra <= 0:
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
    quick_generations[user_id] = quick_genaratus
  genereteoese = int(quick_generations[user_id])
  if genereteoese <= 0:
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
  bot.send_message(message.chat.id, "Я RubiGen, можу генерувати зображення по їх опису.\n\nПідпишіться на Канал RubiGen: @RubiGenChanel.\nЧат RubiGen: @RubiGenChat - Там роздають промокоди на генерацію зображень.\n\nКоманди:\n/buy - ❤Купити Premium підписку на бота RubiGen❤\n/gen - Генерувати зображення.\n/help - Допомога та команди.\n/balance - Перевірити баланс.\n/promo - Ввести промокод.\n/promter - (BETA) Покращиити промт за допомогою PROmter.\n/ref - Отримати рефиральне посилання.\n\nЗа питаннями та допомогою звертайтесь до адміна: @RubiGenSupport.\n")

# Функція для обробки команди перевірки залишку генерацій
def check_generations(message):
    user_id = message.from_user.id

    # Перевірка наявності користувача
    if user_id not in generations:
        generations[user_id] = genaratus
        quick_generations[user_id] = quick_genaratus

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
    for user_id in all_users:
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
  global quick_genaratus
  global genaratus
  user_id = message.chat.id
  if quick_generations[user_id] > quick_genaratus:
    if generations[user_id] > genaratus:
      bot.send_message(message.chat.id, f"Ви не можите активувати ніякі промокоди, тому що: промокоди відновлюють генерації зображень, а у вас наразі більше ніж ***{genaratus}*** повільних та ***{quick_genaratus}*** швидких генерацій.", parse_mode="Markdown")
      return
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
    generations[user_id] = genaratus
    quick_generations[user_id] = quick_genaratus

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
    user_d = message.chat.id
    if user_d == 6133407632:
      bot.send_message(message.chat.id, "Введіть телеграм id нового premium користувача:")
      bot.register_next_step_handler(message, next_add_buy)
    else:
        bot.send_message(message.chat.id, f"Premium підписка RubiGen Basic - Включає в себе ***50*** швидких генерацій, ***100*** повільних та велику нашу подяку.\n\nЩоб купити Premium підписку на нашого бота вам потрібно перевести 100грн на номер картки: `5375414122338071`\nЗ ось таким описом: `Оплата за Premium Basic: {message.chat.id}`\n\nПісля здійснення оплати вам прийде повідомлення про нарахування генерацій.\n\nЯкщо ви через 24 години ви не отримали одобрення платежу тоді зверніться до адміна: @RubiGenSupport.", parse_mode="Markdown")

def next_add_buy (message):
  global usertelegids
  global userbuyid
  userbuyid = message.text
  usertelegids.append(userbuyid)
  bot.send_message(message.chat.id, f"Premium користувача з таким id: `{userbuyid}` додано успішно.", parse_mode="Markdown")
  try:
    typeint = int(userbuyid)
    generations[typeint] = 100
    quick_generations[typeint] = 50
    bot.send_message(userbuyid, f"🎉Оплата пройшла успішно!\n\n💬Вам на баланс нараховано: ***{quick_generations[typeint]}*** ШВИДКИХ ТА ***{generations[typeint]}*** ПОВІЛЬНИХ ГЕНЕРАЦІЙ💬\n\n♥️Дякуємо що користуєтесь нашим телеграм ботом♥️", parse_mode="Markdown")
  except:
    bot.send_message(message.chat.id, f"Користувача з таким id: `{userbuyid}`, немає або користувач НЕ запустив бота.", parse_mode="Markdown")


@bot.message_handler(commands=["ref"])
def send_refrence(message):
    bot.send_message(message.chat.id, f"🎁 Реферальна програма:\n\n💡 Твоїм рефералом вважається будь-який користувач, який уперше потрапив у систему через твоє посилання.\n\n🔗Ваше реферальне посилання: `https://t.me/imagenerabot?start={message.chat.id}`\n\nЗа кожну людину яка приєднається до нашого бота по вашому посиланю, ви отримаєте ***5*** швидких та ***10*** повільних генерацій.", parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def send_awesome(message):
  user_d = message.chat.id
  user_id = message.from_user.id
  try:
    text = message.text.split(' ')[1]
  except:
    if user_id in all_users:
      bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
    elif user_d not in all_users:
        # Запис ID користувача в файл
        with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

        # Додавання ID користувача до списку
        all_users.append(user_id)
        bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
    # Створення запису для нового користувача
    if user_id not in generations:
        generations[user_id] = genaratus
        quick_generations[user_id] = quick_genaratus
    return
  idus = f"{message.chat.id}"
  if idus == text:
    bot.send_message(message.chat.id, "Це ваше реферальне посилання, ви не можете його активувати!")
    all_users.append(user_id)
    return

  else:
    if user_id in all_users:
      bot.send_message(message.chat.id, "Ви вже є нашим рефералом, ви не можете перейти на іншого реферала!")
      all_users.append(user_id)
    else:
      try: 
        bot.send_message(text, "Користувач перейшов по вашому посиланню, ви отримуєте ***5*** швидких та ***10*** повільних генерацій.", parse_mode="Markdown")
        typeint = int(text)
        generations[typeint] = 10
        quick_generations[typeint] = 5
        bot.send_message(message.chat.id, "Ви успішно стали рефиралом стали рефералом, дякуємо вам.")
        if user_id in all_users:
          bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
        elif user_d not in all_users:
            # Запис ID користувача в файл
            with open("users.txt", "a") as f:
                f.write(f"{user_id}\n")

            # Додавання ID користувача до списку
            all_users.append(user_id)
            bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
        # Створення запису для нового користувача
        if user_id not in generations:
            generations[user_id] = genaratus
            quick_generations[user_id] = quick_genaratus
        
      except:
        if user_id in all_users:
          bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
        elif user_d not in all_users:
            # Запис ID користувача в файл
            with open("users.txt", "a") as f:
                f.write(f"{user_id}\n")

            # Додавання ID користувача до списку
            all_users.append(user_id)
            bot.reply_to(message, f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {quick_genaratus} швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.", parse_mode="HTML")
        # Створення запису для нового користувача
        if user_id not in generations:
            generations[user_id] = genaratus
            quick_generations[user_id] = quick_genaratus





    # Додайте код для виконання дії після активації промокоду,
    # наприклад, надання знижки, доступу до контенту тощо.
# Функція для обробки команди start






dobre_id = 0
kilkist_povilnogo_dobra_generatus = 0
kilkist_shvidkogo_dobra_generatus = 0

@bot.message_handler(commands=['free'])
def nashe_dobro_povertaitsya(message):
    global usertelegids
    user_d = message.chat.id
    if user_d == 6133407632:
      bot.send_message(message.chat.id, "Введіть телеграм id користувача якому хочете надати генерації:")
      bot.register_next_step_handler(message, add_id_dobro)


def add_id_dobro(message):
  global dobre_id
  dobre_id = message.text
  bot.send_message(message.chat.id, "Введіть скільки ШВИДКИХ генерацій ви хочете надати цьому користувачу:")
  bot.register_next_step_handler(message, add_genaratus_dobro_1)


def add_genaratus_dobro_1(message):
  global kilkist_shvidkogo_dobra_generatus
  kilkist_shvidkogo_dobra_generatus = message.text
  bot.send_message(message.chat.id, "Введіть скільки ПОВІЛНИХ генерацій ви хочете надати цьому користувачу:")
  bot.register_next_step_handler(message, add_genaratus_dobro)

def add_genaratus_dobro(message):
  kilkist_povilnogo_dobra_generatus = message.text
  try:
    inttype = int(dobre_id)
    bot.send_message(dobre_id, f"🎉Вам нараховано ***{kilkist_shvidkogo_dobra_generatus}*** швидких та ***{kilkist_povilnogo_dobra_generatus}*** повільних генерацій🎉", parse_mode="Markdown")
    bot.send_message(message.chat.id, f"Користувачу надано ***{kilkist_shvidkogo_dobra_generatus}*** швидких та ***{kilkist_povilnogo_dobra_generatus}*** повільних генерацій.", parse_mode="Markdown")
    generations[inttype] = kilkist_povilnogo_dobra_generatus
    quick_generations[inttype] = kilkist_shvidkogo_dobra_generatus
  except:
    inttype = int(dobre_id)
    bot.send_message(message.chat.id, f"Користувача з таким id: `{inttype}`, немає або користувач НЕ запустив бота.", parse_mode="Markdown")





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

