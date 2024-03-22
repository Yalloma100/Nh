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
    


# Функція для обробки натискань на кнопки
@bot.message_handler(func=lambda message: message.text in ["Швидка генерація", "Повільна генерація"])
def handle_buttons(message):
      if message.text == "Швидка генерація":
          # Створення клавіатури для видалення
          keyboard_remove = types.ReplyKeyboardRemove()
          bot.send_message(message.chat.id, "Введіть промт для генерації👇", reply_markup=keyboard_remove)
          bot.register_next_step_handler(message, bumon2)
      elif message.text == "Повільна генерація":
        keyboard_remove = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введіть промт для генерації👇", reply_markup=keyboard_remove)
        bot.register_next_step_handler(message, bumon1)

def bumon1 (message):
  prompt = message.text
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in generations:
      generations[user_id] = 10
     
  if generations[user_id] <= 0:
      bot.send_message(message.chat.id, "Ви вже використали всі генерації на день.")
      return
  bot.send_message(message.chat.id, "Почалась повільна генерація, зазвичай вона йде до 5 хвилин")
  # Зменшення кількості генерацій
  generations[user_id] -= 1

  # Генерація зображення
  prompt = message.text

  try:
    time.sleep(100)
    from gradio_client import Client

    client = Client("ByteDance/SDXL-Lightning")
    result = client.predict(
        prompt,	# str  in 'Enter your prompt (English)' Textbox component
        "8-Step",	# Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
        api_name="/generate_image"
    )
    url = "https://bytedance-sdxl-lightning.hf.space/file=" + result
    time.sleep(5)
    bot.send_photo(message.chat.id, url)
    bot.send_message(message.chat.id, f'У вас залишилося {generations[user_id]} повільних генерацій.')
  except:
    bot.send_message(message.chat.id, "Error")



def bumon2 (message):
  user_id = message.from_user.id
  # Перевірка залишку генерацій
  if user_id not in quick_generations:
    quick_generations[user_id] = 5

  if quick_generations[user_id] <= 0:
      bot.send_message(message.chat.id, "Ви вже використали всі генерації на день.")
      return
  bot.send_message(message.chat.id, "Почалась швидка генерація, зазвичай вона йде до 2 хвилин")
  # Зменшення кількості генерацій
  quick_generations[user_id] -= 1

  # Генерація зображення
  prompt = message.text
  try:
    time.sleep(35)
    from gradio_client import Client

    client = Client("ByteDance/SDXL-Lightning")
    result = client.predict(
        prompt,	# str  in 'Enter your prompt (English)' Textbox component
        "8-Step",	# Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
        api_name="/generate_image"
    )
    url = "https://bytedance-sdxl-lightning.hf.space/file=" + result
    time.sleep(5)
    bot.send_photo(message.chat.id, url)
    bot.send_message(message.chat.id, f'У вас залишилося {quick_generations[user_id]} швидких генерацій.')
  except:
                  bot.send_message(message.chat.id, "Error")

def help(message):
  bot.send_message(message.chat.id, "Я RubiGen, я можу генерувати зображення по їх опису.\n\nКоманди:\n/buy - ❤купити Premium підписку на бота RubiGen❤\n/gen - генерація зображення.\n/help - Допомога та команди.\n/balance - Перешлянути скільки залишилось генерацій на день.\n/promo - Ввести промокод.\n\nЧасті запитання:\nЧому RubiGen не розуміє що я хочу намалювати?\nВідповідь: Промт потрібно писати англійською та більше деталізувати зображення.\nЗа іншими питаннями звертайтесь до адміна: @RubiGenSupport.\nКанал RubiGen: @RubiGenChanel.\nЧат RubiGen: @RubiGenChat.")

# Функція для обробки команди перевірки залишку генерацій
def check_generations(message):
    user_id = message.from_user.id

    # Перевірка наявності користувача
    if user_id not in generations:
        generations[user_id] = 10
        quick_generations[user_id] = 5

    # Повідомлення про залишок генерацій
    bot.send_message(message.chat.id, f"У вас на балансі {quick_generations[user_id]} швидких генерацій та {generations[user_id]} повільних генерацій.")

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
        bot.send_message(message.chat.id, f"Вам на баланс начислено {quick_generations[user_id]} швидких генерацій та {generations[user_id]} повільних генерацій.\n\nДякуємо що користуєтесь нашим телеграм ботом.")
      else:
        bot.send_message(message.chat.id, f"Premium підписка RubiGen Basic - Включає в себе 200 швидких генерацій, 400 повільних та велику нашу подяку.\n\nЩоб купити Premium підписку на нашого бота вам потрібно перевести 100грн на номер картки: 5375414122338071\nЗ ось таким описом: <b>Оплата за Premium Basic: {message.chat.id}</b>\n\nПісля переводу грошей вам потрібно очікувати до 24 годин, після вам прийде повідомлення про одобрення платежу.\n\nЯкщо ви через 24 години не отримали одобрення платежу тоді зверніться до адміна: @RubiGenSupport.", parse_mode="HTML")
        
def next_add_buy (message):
  global usertelegids
  global userbuyid
  userbuyid = message.text
  usertelegids.append(userbuyid)
  bot.send_message(message.chat.id, "Користувача додано до списку.")
  bot.send_message(userbuyid, "Вам підтвердили оплату premium підписки.\n\n!!!ВВЕДІТЬ КОМАНДУ /buy ЩОБ ОТРИМАТИ: 200 ШВИДКИХ ТА 400 ПОВІЛЬНИХ ГЕНЕРАЦІЙ!!!\n\nДякуємо що користуєтесь нашим телеграм ботом.")

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
        bot.reply_to(message, "Привіт, я бот, який може безкоштовно генерувати зображення. У вас 5 швидкісних генерацій та 10 повільних. Введіть команду /help щоб почати.")
    # Створення запису для нового користувача
    if user_id not in generations:
        generations[user_id] = 10
        quick_generations[user_id] = 5




keep_alive()

while True:
  try:
      bot.polling(none_stop=True)
  except Exception as e:
      print(f"Помилка: {e}")
      time.sleep(1)
