import telebot
from telebot import types

bot = telebot.TeleBot('5538649868:AAEhKN8FauGRwBlvNI2ZsclQxltxy9TrFlE')


@bot.message_handler(commands=['start'])  # запуск
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>, жопу мыл?"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])  # реакция на текст
def get_user_text(message):
    if "да" in message.text.lower() or "yep" in message.text.lower() or "yes" in message.text.lower() or message.text.lower() == "мыл" or message.text.lower() == "мыла":
        # if message.text.lower() == "да": - ну вот хз как это лучше прописать
        bot.send_message(message.chat.id, "Молодец, держи жабу", parse_mode='html')
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGY4hjb0fjc7s73RFY65mE7NINXf8uVAACCgoAAkz_kEsm-kgd8qwSrisE")
    elif "нет" in message.text.lower() or "не" in message.text.lower() or "no" in message.text.lower():
        # elif message.text.lower() == "нет" or message.text.lower() == "неа": - ну вот хз как это лучше прописать №2
        bot.send_message(message.chat.id, "Иди мой", parse_mode='html')
    elif message.text.lower() == "спасибо" or message.text.lower() == "ок" or message.text.lower() == "ok":
        bot.send_message(message.chat.id, "Всё ради чистых жоп, мой друг!", parse_mode='html')
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Жопки ответ", parse_mode='html')
    elif message.text.lower() == "пока" or message.text.lower() == "прощай":
        bot.send_message(message.chat.id, "Покусики, в попе трусики", parse_mode='html')
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGZDFjb13Bg3cYuOuXikxF0dxOYD51jwAC_w4AAuHC4Er4350bH5-0qCsE")
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Как помыть жопу", url="https://youtu.be/gmHQi5Smc0Q"))
        bot.send_message(message.chat.id, "Нужна помощь? Вот линк:", reply_markup=markup)


# bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html') - оригинальный вариант для else

@bot.message_handler(content_types=['photo'])  # реакция на фото
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау, крутое фото! Давай жопу теперь")


@bot.message_handler(content_types=['sticker'])  # реакция на стикер
def sticker_id(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGY4Rjb0bNSjfffzCzeeCL2rvWs-4rIAACHAsAAqYE6EoR-fwy7VgywisE")


# @bot.message_handler(commands=['website']) - добавить линк
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Как помыть жопу", url="https://youtu.be/gmHQi5Smc0Q"))
#     bot.send_message(message.chat.id, "Нужна помощь?", reply_markup=markup)

# @bot.message_handler(commands=['help']) - кнопки помощи
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('Веб сайт')
#     start = types.KeyboardButton('Старт')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Нужна помощь?", reply_markup=markup)

bot.polling(none_stop=True)
