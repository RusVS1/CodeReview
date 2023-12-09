import telebot
from telebot import types
from parse import *
from database import *

bot = telebot.TeleBot('6678156658:AAE85YEYUFTu9sa0dzQyF32oW13OsogMp_M')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    atlas = types.KeyboardButton('Атлас')
    banshee = types.KeyboardButton('Банши')
    baruuk = types.KeyboardButton('Баруук')
    valkyr = types.KeyboardButton('Валькирия')
    wisp = types.KeyboardButton('Висп')
    vauban = types.KeyboardButton('Вобан')
    volt = types.KeyboardButton('Вольт')
    wukong = types.KeyboardButton('Вуконг')
    gara = types.KeyboardButton('Гара')
    garuda = types.KeyboardButton('Гаруда')
    hydroid = types.KeyboardButton('Гидроид')
    grendel = types.KeyboardButton('Грендель')
    zephyr = types.KeyboardButton('Зефир')
    ivara = types.KeyboardButton('Ивара')
    inaros = types.KeyboardButton('Инарос')
    khora = types.KeyboardButton('Кора')
    limbo = types.KeyboardButton('Лимбо')
    loki = types.KeyboardButton('Локи')
    mirage = types.KeyboardButton('Мираж')
    mesa = types.KeyboardButton('Миса')
    mag = types.KeyboardButton('Мэг')
    nekros = types.KeyboardButton('Некрос')
    nidus = types.KeyboardButton('Нидус')
    nyx = types.KeyboardButton('Никс')
    nova = types.KeyboardButton('Нова')
    nezha = types.KeyboardButton('Нэчжа')
    oberon = types.KeyboardButton('Оберон')
    octavia = types.KeyboardButton('Октавия')
    revenant = types.KeyboardButton('Ревенант')
    rhino = types.KeyboardButton('Рино')
    saryn = types.KeyboardButton('Сарина')
    titania = types.KeyboardButton('Титания')
    trinity = types.KeyboardButton('Тринити')
    frost = types.KeyboardButton('Фрост')
    harrow = types.KeyboardButton('Харроу')
    hildryn = types.KeyboardButton('Хильдрин')
    chroma = types.KeyboardButton('Хрома')
    equinox = types.KeyboardButton('Эквинокс')
    ember = types.KeyboardButton('Эмбер')
    ash = types.KeyboardButton('Эш')

    keyboard.add(atlas, banshee, baruuk, valkyr, wisp, vauban, volt, wukong, gara, garuda, 
    hydroid, grendel, zephyr, ivara, inaros, khora, limbo, loki, mirage, mesa, mag, nekros, 
    nidus, nyx, nova, nezha, oberon, octavia, revenant, rhino, saryn, titania, trinity, frost, 
    harrow, hildryn, chroma, equinox, ember, ash)

    bot.send_message(message.chat.id, "Привет! Я телеграмм бот.\nОтправь мне имя варфрейма или воспользуйся кнопками и я выведу тебе, как выгоднее купить!", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    frame = message.text
    frame = get_frame_name(frame)
    if frame != "frame_missing":
        bot.send_message(message.chat.id, "Ищу цены...")
        find_prices(frame)
        name, sets, bluep, neuro, systm, chas = get_prices(frame)
        bot.send_message(message.chat.id, f"""Варианты покупки:
Весь комплект одним обменом - {sets}пл.
Каждую часть отдельно - {bluep + neuro + systm + chas}пл.
    Основной чертёж - {bluep}пл.
    Нейрооптика - {neuro}пл.
    Система - {systm}пл.
    Каркас - {chas}пл.
""")
    else:
        bot.send_message(message.chat.id, "Такого варфрейма нет! Попробуй еще раз.")

bot.polling(none_stop=True)