from logging import getLogger
import os
import requests
import telebot
import time
import threading

from telebot.util import quick_markup
from background import keep_alive
from telebot import types

BOT_TOKEN = "6754268225:AAFN5qOtXqjMemojBbY0pIHhzJWc1AH1fCI"  # Замініть це своїм токеном бота
bot = telebot.TeleBot(BOT_TOKEN)

genaratus = 5
phone_number = None
myid = [6133407632]
numbon = 0
illo = 0
keys = [
    "sk-a2XTgMvnn3xsbjyqxarwIM141g627uqyh2ixpYi1DbkfSBHt",
    "sk-F2266cS4CWFmuBzgVsY7O7SRiVTBhimVaHOUgvPXZmYV0ixh",
    "sk-Z8cpp04jw5GiPuVcpwNoz35GhLJlpMUbclpqAodFuWYO3lfF",
    "sk-TSYpJALg4B16twcexaoe42jRxf6F791ndKn0EvoLhxE7hY0O",
    "sk-FyLFUvAgxfTxitTnn93lq46VgnCv4oVvK4CoCJIl6gxtBkdQ",
    "sk-lTbrGsGeKw2kIf1dLcbksNqpc8p2xYq4eg1pYE7bARpEy0gj",
    "sk-j7mlko4ial8Qx5S6nA4b9zl0ia885Btu85GCreSp6dXUISAb",
    "sk-PYHffx0JIe2EM75GH2zax6mU5RYb3uz9bjCLdMa86Rbh1PiY",
    "sk-gy3ufunqVTF6TVssRpYjUyop3N0phIBrreGBnt8oEANiW9Dt",
    "sk-INTOAi19LNZ3lpLoIfudOuH5rrct3vsOuKaqExQDnW9H1VoZ",
    "sk-FVlWPqufhMgRN3WzTZoCXKi4IybQrOrIv9YLqX8CMBCoT7lM",
    "sk-WgdoQyjywKeNK1pRQf02FT7AdxqsJiYOGiq3cQn5WxwBvOX2",
    "sk-QCVQ0PVYCbXwEsvGCDqxpjovpBNrHCX3aa8ZPpN2esKTYWue",
    "sk-HLf4j5gLaFDbKRsCAhs0EZT1XZxzJcJJAXgWfoOZe0Byrk0B",
    "sk-t9buh9V5u0lhaWyiugJBRltcEYJnjWZHh9129plouJBwOViQ",
    "sk-nPQfH9RsXvylgwGPH1utUoDfmdJ3xuW7vf9G5n9q3x3VMnHk",
    "sk-1a0qO9YN0EMoIHqS943Z5X2qooyIM3ztqtaFN1oVzQNJzJYX",
    "sk-7wBFp3o5bkfvOXmQDDBo18iXDLtfFplVEplsFUsLvS3tKOe2",
    "sk-9S3eJoU78CwPW74BBaSeJzmeZf9QOEHmCKLSGvXoOcV2u6KK",
    "sk-8aEWXvsOeIUmTZXDO6vzKl6lllbQc6De2iAxPoQyw1M7BCLG",
    "sk-3jEtVIxy83PZdYCcg4eYOVO3ide53A7KJQDYWpHSebW6YDnl",
    "sk-PBhcupWfxvs6gEUZz77wKnpXmrJ7gXvAton47CqCh3GaiMwd",
    "sk-sXIgnZh5TZoQ8U0QKTNNfboXL3Vq3zwtFgTCUFGC5CIq2rvI",
    "sk-LivdKXpYUX24ig48kaY0ZL3RYa54TOlSpp7LQPWZxxn21OzS",
    "sk-5AFzY3keaHV8RaauJbZGunlCdeLT295Z0subZNpz0o0fD0e3"
]

keycode = "sk-SIU50qnpeIFOFGa7G20COSIa9pPxIwAKG6i8ASvy728Njj9d"
keycodeforreserch = "sk-Yp8MZxLGNSwQl1fhbaR4KAp1SwhBJl12CwnRDj4GBgicTFP1"
startuser = []
addpromocodesss = ""
usernameid = ""

# Створення словника для зберігання інформації про генерації
generations = {}


@bot.message_handler(commands=['gen'])
# Функція для обробки команди генерації зображення
def generate_image(message):
  global genaratus
  user_id = message.from_user.id
  user_d = message.chat.id
  # Створення двох кнопок
  button_1 = types.KeyboardButton("Звичайна генерація")
  button_2 = types.KeyboardButton("Search and Replace")
  button_3 = types.KeyboardButton("SDXL diffusion")
  button_4 = types.KeyboardButton("Stable Cascade")
  button_5 = types.KeyboardButton("SDXL-Lightning")
  # Створення клавіатури з двома рядами
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  keyboard.add(button_1)
  keyboard.add(button_3)
  keyboard.add(button_4)
  keyboard.add(button_5)

  # Відправлення повідомлення з двома кнопками
  if user_id in all_users:
    bot.send_message(message.chat.id,
                     "Виберіть яку генерацію ви хочете використати👇",
                     reply_markup=keyboard)
  elif user_d not in all_users:
    # Запис ID користувача в файл
    with open("users.txt", "a") as f:
      f.write(f"{user_id}\n")

    # Додавання ID користувача до списку
    all_users.append(user_id)
    bot.send_message(message.chat.id,
                     "Виберіть яку генерацію ви хочете використати👇",
                     reply_markup=keyboard)
  # Створення запису для нового користувача
  if user_id not in generations:
    generations[user_id] = genaratus


# Функція для обробки натискань на кнопки
@bot.message_handler(func=lambda message: message.text in [
    "Search and Replace", "Звичайна генерація", "SDXL diffusion",
    "Stable Cascade", "SDXL-Lightning"
])
def handle_buttons(message):
  user_id = message.from_user.id
  user_d = message.chat.id
  if user_id in all_users:
    if message.text == "Search and Replace":
      # Створення клавіатури для видалення
      keyboard_remove = types.ReplyKeyboardRemove()
      bot.send_message(message.chat.id,
                       "Надішліть фото для заміни об'єкту👇",
                       reply_markup=keyboard_remove)
      bot.register_next_step_handler(message, handle_search_and_replace)
    elif message.text == "Звичайна генерація":
      # Створення клавіатури для видалення
      keyboard_remove = types.ReplyKeyboardRemove()
      bot.send_message(message.chat.id,
                       "Введіть промт для генерації👇",
                       reply_markup=keyboard_remove)
      bot.register_next_step_handler(message, bumon1)
    elif message.text == "SDXL diffusion":
      # Створення клавіатури для видалення
      keyboard_remove = types.ReplyKeyboardRemove()
      bot.send_message(message.chat.id,
                       "Введіть промт для генерації👇",
                       reply_markup=keyboard_remove)
      bot.register_next_step_handler(message, sdxldiffusion)

    elif message.text == "Stable Cascade":
      # Створення клавіатури для видалення
      keyboard_remove = types.ReplyKeyboardRemove()
      bot.send_message(message.chat.id,
                       "Введіть промт для генерації👇",
                       reply_markup=keyboard_remove)
      bot.register_next_step_handler(message, stablecascade)
    elif message.text == "SDXL-Lightning":
      # Створення клавіатури для видалення
      keyboard_remove = types.ReplyKeyboardRemove()
      bot.send_message(message.chat.id,
                       "Введіть промт для генерації👇",
                       reply_markup=keyboard_remove)
      bot.register_next_step_handler(message, sdxllightning)
  elif user_d not in all_users:
    # Запис ID користувача в файл
    with open("users.txt", "a") as f:
      f.write(f"{user_id}\n")
  # Додавання ID користувача до списку
    all_users.append(user_id)
    handle_buttons(message)


def sdxllightning(message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in generations:
    generations[user_id] = genaratus

  if generations[user_id] <= 0:
    bot.send_message(message.chat.id, "Ви вже використали всі генерації.")
    return
  bot.send_message(message.chat.id, "Почалась генерація...")
  user_id = message.chat.id
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')
  prompt = resut
  try:
    from gradio_client import Client

    client = Client("cbensimon/Real-Time-Text-to-Image-SDXL-Lightning")
    result = client.predict(
        prompt,  # str  in 'parameter_5' Textbox component
        0,  # float (numeric value between 0 and 12013012031030) in 'Seed' Slider component
        api_name="/predict")
    url = "https://cbensimon-real-time-text-to-image-sdxl-lightning.hf.space/file=" + result
    bot.send_photo(
        message.chat.id,
        url,
        caption=
        f"💬Prompt:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** генерацій.",
        parse_mode="Markdown")
    generations[user_id] -= 1
  except:
    bot.send_message(
        message.chat.id,
        "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport."
    )


def sdxldiffusion(message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in generations:
    generations[user_id] = genaratus

  if generations[user_id] <= 0:
    bot.send_message(message.chat.id, "Ви вже використали всі генерації.")
    return
  bot.send_message(message.chat.id, "Почалась генерація...")
  user_id = message.chat.id
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')
  prompt = resut
  try:
    from gradio_client import Client

    client = Client("ahmedemara10/Dremmar-nsfw-xl")
    result = client.predict(
        prompt,  # str  in 'Input' Textbox component
        api_name="/predict")
    url = "https://ahmedemara10-dremmar-nsfw-xl.hf.space/file=" + result
    bot.send_photo(
        message.chat.id,
        url,
        caption=
        f"💬Prompt:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** генерацій.",
        parse_mode="Markdown")
    generations[user_id] -= 1
  except:
    bot.send_message(
        message.chat.id,
        "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport."
    )


def stablecascade(message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in generations:
    generations[user_id] = genaratus

  if generations[user_id] <= 0:
    bot.send_message(message.chat.id, "Ви вже використали всі генерації.")
    return
  bot.send_message(message.chat.id, "Почалась генерація...")
  user_id = message.chat.id
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')
  prompt = resut
  try:
    from gradio_client import Client

    client = Client("ddosxd/stable-cascade")
    result = client.predict(
        prompt,  # str  in 'Prompt' Textbox component
        "",  # str  in 'Negative prompt' Textbox component
        0,  # float (numeric value between 0 and 2147483647) in 'Seed' Slider component
        1024,  # float (numeric value between 1024 and 1536) in 'Width' Slider component
        1024,  # float (numeric value between 1024 and 1536) in 'Height' Slider component
        10,  # float (numeric value between 10 and 30) in 'Prior Inference Steps' Slider component
        0,  # float (numeric value between 0 and 20) in 'Prior Guidance Scale' Slider component
        4,  # float (numeric value between 4 and 12) in 'Decoder Inference Steps' Slider component
        0,  # float (numeric value between 0 and 0) in 'Decoder Guidance Scale' Slider component
        1,  # float (numeric value between 1 and 2) in 'Number of Images' Slider component
        api_name="/run")
    url = "https://ddosxd-stable-cascade.hf.space/file=" + result
    bot.send_photo(
        message.chat.id,
        url,
        caption=
        f"💬Prompt:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** генерацій.",
        parse_mode="Markdown")
    generations[user_id] -= 1
  except:
    bot.send_message(
        message.chat.id,
        "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport."
    )


def handle_search_and_replace(message):
  try:
    # Отримуємо ID чату та ID фото
    photo_id = message.photo[-1].file_id
    # Отримуємо об'єкт фото за ID
    photo_info = bot.get_file(photo_id)
    photo_file = bot.download_file(photo_info.file_path)
    # Зберігаємо фото з назвою ./husky-in-a-field.png
    with open("./husky-in-a-field.png", 'wb') as new_file:
      new_file.write(photo_file)
    bot.send_message(message.chat.id,
                     "Введіть назву об'єкта який ви хочете замінити👇")
    bot.register_next_step_handler(message, reg_promt_img)
  except Exception as e:
    bot.send_message(message.chat.id,
                     "Помилка при отриманні фото. Спробуйте ще раз.")


def reg_promt_img(message):
  search_promp = message.text
  bot.send_message(message.chat.id, "Введіть на що ви хочете замінити👇")
  bot.register_next_step_handler(message, reg_promt_img2, search_promp)


def reg_promt_img2(message, search_promp):
  user_id = message.from_user.id
  prompt = message.text
  if user_id not in generations:
    generations[user_id] = genaratus

  if generations[user_id] <= 0:
    bot.send_message(message.chat.id, "Ви вже використали всі генерації.")
    return
  bot.send_message(message.chat.id, "Почалась генерація...")
  try:
    from easygoogletranslate import EasyGoogleTranslate
    translator = EasyGoogleTranslate()
    resut = translator.translate(prompt, target_language='en')
    prompt = resut
    translator = EasyGoogleTranslate()
    resut = translator.translate(search_promp, target_language='en')
    search_promp = resut

    global keycodeforreserch

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/edit/search-and-replace",
        headers={
            "authorization": keycodeforreserch,
            "accept": "image/*"
        },
        files={"image": open("./husky-in-a-field.png", "rb")},
        data={
            "prompt": prompt,
            "search_prompt": search_promp,
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
      with open("./golden-retriever-in-a-field.webp", 'wb') as file:
        file.write(response.content)
    else:
      raise Exception(str(response.json()))

    url = open('./golden-retriever-in-a-field.webp', 'rb')
    bot.send_photo(
        message.chat.id,
        url,
        caption=
        f"💬Prompt:` {prompt}\n`💬Search prompt: `{search_promp}`\n\n💰У вас залишилося ***{generations[user_id] - 1}*** генерацій.",
        parse_mode="Markdown")
    generations[user_id] -= 1
  except:
    bot.send_message(
        message.chat.id,
        "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport."
    )


def bumon1(message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in generations:
    generations[user_id] = genaratus

  if generations[user_id] <= 0:
    bot.send_message(message.chat.id, "Ви вже використали всі генерації.")
    return
  bot.send_message(message.chat.id, "Почалась генерація...")
  user_id = message.chat.id
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(prompt, target_language='en')
  prompt = resut
  try:
    from gradio_client import Client

    client = Client("mexicanamerican/dalle-3-xl-lora-v2")
    result = client.predict(
		prompt,	# str in 'Prompt' Textbox component
		"(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, (NSFW:1.25)",	# str in 'Negative prompt' Textbox component
		True,	# bool in 'Use negative prompt' Checkbox component
		0,	# float (numeric value between 0 and 2147483647)
								#in 'Seed' Slider component
		1024,	# float (numeric value between 512 and 2048)
								#in 'Width' Slider component
		1024,	# float (numeric value between 512 and 2048)
								#in 'Height' Slider component
	  6.0,	# float (numeric value between 0.1 and 20.0)
								#in 'Guidance Scale' Slider component
		True,	# bool in 'Randomize seed' Checkbox component
		api_name="/run"
)
    my_string= str(result)
    start_marker = "/tmp/gradio/"
    end_marker = ".png"
    extracted_value = my_string.split(start_marker)[1].split(end_marker)[0]

# Помещение значения в переменную
    codemmm = extracted_value

    url = "https://mexicanamerican-dalle-3-xl-lora-v2.hf.space/file=" + "/tmp/gradio/" + codemmm + ".png"

    # Видаліть останнє повідомлення, яке ваш бот відправив у чат користувача
    bot.send_photo(
        message.chat.id,
        url,
        caption=
        f"💬Промт:` {prompt}\n`\n💰У вас залишилося ***{generations[user_id] - 1}*** повільних генерацій.",
        parse_mode="Markdown")
    generations[user_id] -= 1
  except:
    bot.send_message(
        message.chat.id,
        "Помилка генерації зображення, можливо ваш промт порушує наші правила, перевірте промт та спробуйте ще раз.\n\nЯкщо помилка повторилася, зверніться до адміна: @RubiGenSupport."
    )

# Зменшення кількості генерацій


def help(message):
  bot.send_message(
      message.chat.id,
      "Я RubiGen, можу генерувати зображення по їх опису.\n\nПідпишіться на Канал RubiGen: @RubiGenChanel.\nЧат RubiGen: @RubiGenChat - Там роздають промокоди на генерацію зображень.\n\nКоманди:\n/buy - ❤Купити Premium підписку на бота RubiGen❤\n/gen - Генерувати зображення.\n/help - Допомога та команди.\n/balance - Перевірити баланс.\n/promo - Ввести промокод.\n/promter - (BETA) Покращиити промт за допомогою PROmter.\n/ref - Отримати рефиральне посилання.\n\n*new:\n/gpt - Задати питання gpt.\n/qwen - Задати питання Qwen.\n/llama - Задати питання Llama 3.\n\nЗа питаннями та допомогою звертайтесь до адміна: @RubiGenSupport.\n"
  )


# Функція для обробки команди перевірки залишку генерацій
def check_generations(message):
  user_id = message.chat.id
  global generations
  # Перевірка наявності користувача
  if user_id not in generations:
    generations[user_id] = genaratus

  # Повідомлення про залишок генерацій
  bot.send_message(
      message.chat.id,
      f"💰Наразі у вас на балансі: ***{generations[user_id]}*** генерацій.",
      parse_mode="Markdown")


# Реєстрація команд
bot.register_message_handler(check_generations, commands=['balance'])
bot.register_message_handler(help, commands=['help'])

all_users = []


@bot.message_handler(commands=['llama'])
def llama_chat(message):
  bot.send_message(message.chat.id, "Введіть запит до Llama👇")
  bot.register_next_step_handler(message, gpt_send)


def llama_send(message):
  text_to_gpt = message.text
  bot.send_message(message.chat.id, "💬Відповідаю...")
  from gradio_client import Client

  client = Client("ysharma/Chat_with_Meta_llama3_8b")
  result = client.predict(message=text_to_gpt,
                          request=0.95,
                          param_3=512,
                          api_name="/chat")
  answer_gpt = result
  bot.send_message(message.chat.id, answer_gpt, parse_mode="Markdown")


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
  bot.send_message(
      message.chat.id,
      f"Ключ додано.\n\nУ вас залишилось {numbon} працюючих ключів\n\n\nКлючі:\n"
      + "\n".join(keys))


# Змінна для зберігання промокодів
promocodes = []

# Словник для зберігання активованих промокодів
activated_promocodes = {}


@bot.message_handler(commands=["promo"])
def promo_handler(message: types.Message):
  global genaratus
  user_id = message.chat.id
  if generations[user_id] > genaratus:
    bot.send_message(
        message.chat.id,
        f"Ви не можите активувати ніякі промокоди, тому що: промокоди відновлюють генерації зображень, а у вас наразі більше ніж ***{genaratus}*** генерацій.",
        parse_mode="Markdown")
    return
  try:
    # Отримання тексту повідомлення
    text = message.text.split(' ')[1]
  except:
    bot.send_message(
        message.chat.id,
        "Вводьте в такому форматі: \n/promo code, на місті \"code\" вставте ваш промокод."
    )
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
    bot.send_message(message.chat.id,
                     "Введіть телеграм id нового premium користувача:")
    bot.register_next_step_handler(message, next_add_buy)
  else:
    bot.send_message(
        message.chat.id,
        f"Premium підписка RubiGen Basic - Включає в себе: ***100*** генерацій та велику нашу подяку.\n\nЩоб купити Premium підписку на нашого бота вам потрібно перевести 100грн на номер картки: `5375414122338071`\nЗ ось таким описом: `Оплата за Premium Basic: {message.chat.id}`\n\nПісля здійснення оплати вам прийде повідомлення про нарахування генерацій.\n\nЯкщо ви через 24 години ви не отримали одобрення платежу тоді зверніться до адміна: @RubiGenSupport.",
        parse_mode="Markdown")


def next_add_buy(message):
  global usertelegids
  global userbuyid
  userbuyid = message.text
  usertelegids.append(userbuyid)
  bot.send_message(
      message.chat.id,
      f"Premium користувача з таким id: `{userbuyid}` додано успішно.",
      parse_mode="Markdown")
  try:
    typeint = int(userbuyid)
    generations[typeint] = 100
    bot.send_message(
        userbuyid,
        f"🎉Оплата пройшла успішно!\n\n💬Вам на баланс нараховано: ***{generations[typeint]}*** генерацій💬\n\n♥️Дякуємо що користуєтесь нашим телеграм ботом♥️",
        parse_mode="Markdown")
  except:
    bot.send_message(
        message.chat.id,
        f"Користувача з таким id: `{userbuyid}`, немає або користувач НЕ запустив бота.",
        parse_mode="Markdown")


@bot.message_handler(commands=["ref"])
def send_refrence(message):
  bot.send_message(
      message.chat.id,
      f"🎁 Реферальна програма:\n\n💡 Твоїм рефералом вважається будь-який користувач, який уперше потрапив у систему через твоє посилання.\n\n🔗Ваше реферальне посилання: `https://t.me/imagenerabot?start={message.chat.id}`\n\nЗа кожну людину яка приєднається до нашого бота по вашому посиланю, ви отримаєте 10 генерацій.",
      parse_mode="Markdown")


@bot.message_handler(commands=["start"])
def send_awesome(message):
  user_d = message.chat.id
  user_id = message.from_user.id
  try:
    text = message.text.split(' ')[1]
  except:
    if user_id in all_users:
      bot.reply_to(
          message,
          f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас швидкісних генерацій та {genaratus} повільних.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
          parse_mode="HTML")
    elif user_d not in all_users:
      # Запис ID користувач600а в файл
      with open("users.txt", "a") as f:
        f.write(f"{user_id}\n")

      # Додавання ID користувача до списку
      all_users.append(user_id)
      bot.reply_to(
          message,
          f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {genaratus}  генерацій.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
          parse_mode="HTML")
    # Створення запису для нового користувача
    if user_id not in generations:
      generations[user_id] = genaratus
    return
  idus = f"{message.chat.id}"
  if idus == text:
    bot.send_message(
        message.chat.id,
        "Це ваше реферальне посилання, ви не можете його активувати!")
    all_users.append(user_id)
    return

  else:
    if user_id in all_users:
      bot.send_message(
          message.chat.id,
          "Ви вже є нашим рефералом, ви не можете перейти на іншого реферала!")
      all_users.append(user_id)
    else:
      try:
        bot.send_message(
            text,
            "Користувач перейшов по вашому посиланню, ви отримали ***10*** генерацій.",
            parse_mode="Markdown")
        typeint = int(text)
        generations[typeint] = 10
        bot.send_message(
            message.chat.id,
            "Ви успішно стали рефиралом стали рефералом, дякуємо вам.")
        if user_id in all_users:
          bot.reply_to(
              message,
              f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {genaratus} генерацій.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
              parse_mode="HTML")
        elif user_d not in all_users:
          # Запис ID користувача в файл
          with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

          # Додавання ID користувача до списку
          all_users.append(user_id)
          bot.reply_to(
              message,
              f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {genaratus} генерацій.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
              parse_mode="HTML")
        # Створення запису для нового користувача
        if user_id not in generations:
          generations[user_id] = genaratus

      except:
        if user_id in all_users:
          bot.reply_to(
              message,
              f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {genaratus} генерацій.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
              parse_mode="HTML")
        elif user_d not in all_users:
          # Запис ID користувача в файл
          with open("users.txt", "a") as f:
            f.write(f"{user_id}\n")

          # Додавання ID користувача до списку
          all_users.append(user_id)
          bot.reply_to(
              message,
              f"Вітаємо вас у RubiGen який може безкоштовно генерувати зображення.\nУ вас {genaratus} генерацій.\n\nПриєднайтеся будь ласка до нашого <a href=\"https://t.me/RubiGenChat\">чату</a> та <a href=\"https://t.me/RubiGenChanel\">каналу</a>.\nА потім введіть команду /help.",
              parse_mode="HTML")
        # Створення запису для нового користувача
        if user_id not in generations:
          generations[user_id] = genaratus

    # Додайте код для виконання дії після активації промокоду,
    # наприклад, надання знижки, доступу до контенту тощо.


# Функція для обробки команди start


@bot.message_handler(commands=['gpt'])
def gpt(message):
  bot.send_message(message.chat.id, "Введіть запит до chat gpt👇")
  bot.register_next_step_handler(message, gpt_send)


def gpt_send(message):
  text_to_gpt = message.text
  bot.send_message(message.chat.id, "💬Відповідаю...")
  from g4f.client import Client

  client = Client()
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role": "user",
          "content": text_to_gpt
      }],
  )
  answer_gpt = response.choices[0].message.content
  bot.send_message(message.chat.id, answer_gpt, parse_mode="Markdown")


@bot.message_handler(commands=['qwen'])
def qwen(message):
  bot.send_message(message.chat.id, "Введіть запит до Qwen👇")
  bot.register_next_step_handler(message, qwen_send)


def qwen_send(message):
  text_to_qwen = message.text
  bot.send_message(message.chat.id, "💬Відповідаю...")
  from gradio_client import Client
  client = Client("Qwen/Qwen1.5-32B-Chat-demo")
  result = client.predict(query=text_to_qwen,
                          history=[],
                          system="You helpful assistant Qwen",
                          api_name="/model_chat")
  writed_prompt = result[1][0][1]
  bot.send_message(message.chat.id, writed_prompt, parse_mode="Markdown")


@bot.message_handler(commands=['promter'])
def beta_promter(message):
  bot.send_message(
      message.chat.id,
      "‼Увага‼\nНаразі ***PROmter*** це ***BETA*** версія, іноді може давати неправильні результати!\n\nВведіть ваш промт будь якою мовою, а я спробую його покращити👇",
      parse_mode="Markdown")
  bot.register_next_step_handler(message, promter)


def promter(message):
  chat_text = message.text
  bot.send_message(
      message.chat.id,
      "PROmter зараз займається покращенням вашого промту, зазвичай це триває до 35 секунд."
  )
  from easygoogletranslate import EasyGoogleTranslate
  translator = EasyGoogleTranslate()
  resut = translator.translate(chat_text, target_language='en')

  chat_text = resut
  from gradio_client import Client
  client = Client("Qwen/Qwen1.5-32B-Chat-demo")
  result = client.predict(
      query=chat_text,
      history=[],
      system=
      "Enhance the prompt provided by the user for generating images, adding more details and improving it. Return only the improved prompt without any unnecessary words or punctuation marks.",
      api_name="/model_chat")

  # Виводити лише друге значення (репліку асистента)
  writed_prompt = result[1][0][1]
  bot.send_message(
      message.chat.id,
      f"\****Покращанний промт***: `{writed_prompt}`\n\n\* - іноді PROmter може навпаки, погіршити промт.\n\n\nПриєднайтесь до каналу RubiGen щоб бачити більше новин про оновлення: https://t.me/RubiGenChanel",
      parse_mode="Markdown")


keep_alive()



# Функция, которую вы хотите выполнить в другом потоке
def my_dfggsdfgdsfgdfg():
  while True:
    print("None stope this functhion!")

# Создание потока
thread = threading.Thread(target=my_dfggsdfgdsfgdfg)

# Запуск потока
thread.start()

while True:
  try:
    bot.polling(none_stop=True)
  except Exception as e:
    bot.send_message(6133407632, f"Помилка: {e}")
    time.sleep(1)
