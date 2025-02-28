import random
import telebot
import requests
import os
from bot_logic import gen_pass, gen_emodji, flip_coin

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot('8186614356:AAEAlAGKyIstS6QCOgUEUiJ6HhnlJJFR-tY')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Тут ты можешь узнать о глобальном потеплении. Напиши команду /hello, /bye, /facts, /reasons, /save, /photo, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")
global_warming_facts = [
    "Глобальное потепление вызвано увеличением концентрации парниковых газов в атмосфере.",
    "Глобальное потепление существует: за последние 140 лет среднегодовая температура повысилась примерно на 1°C.",
    "Современное потепление связано с увеличением концентрации парниковых газов в атмосфере, вызванным деятельностью человека.",
    "С 1880 года средняя температура на Земле уже повысилась на 1,2°C из-за выбросов парниковых газов.",
    "Парниковые газы, такие как углекислый газ и метан, задерживают тепло в атмосфере, что приводит к повышению температуры.",
    "По прогнозам климатологов, к концу XXI века глобальная температура может повыситься как минимум на 2,5°C по сравнению с доиндустриальным уровнем.",
    "Изменение климата ведет к повышению уровня моря и увеличению частоты экстремальных погодных явлений, таких как ураганы и засухи.",
    "По данным Всемирной метеорологической организации, концентрация парниковых газов достигла рекорда в последние годы.",
    "Леса играют важную роль в поглощении углекислого газа; их вырубка усугубляет проблему глобального потепления.",
    "Глобальное потепление угрожает биоразнообразию, вызывая исчезновение многих видов животных и растений.",
    "Межправительственная группа экспертов по изменению климата (IPCC) утверждает, что влияние человека является основной причиной изменения климата."
]
global_warming_reasons = [
    "Сжигание ископаемого топлива (уголь, нефть, газ) для производства энергии.",
    "Вырубка лесов (обезлесение) и уничтожение растительности.",
    "Промышленное производство (выбросы парниковых газов).",
    "Сельское хозяйство (выбросы метана и оксида азота).",
    "Транспорт (автомобили, самолеты, корабли).",
    "Производство цемента.",
    "Сжигание отходов.",
    "Добыча и транспортировка ископаемого топлива.",
    "Использование фторсодержащих газов в промышленности и быту.",
    "Интенсивное животноводство (выбросы метана)."
]
save_earth = [
    "Сокращение использования ископаемого топлива и переход на возобновляемые источники энергии.",
    "Увеличение энергоэффективности в домах и на предприятиях.",
    "Посадка деревьев и восстановление лесов.",
    "Снижение потребления мяса и переход на растительную диету.",
    "Использование общественного транспорта, велосипедов или пеших прогулок вместо автомобилей.",
    "Сокращение, повторное использование и переработка отходов.",
    "Поддержка устойчивого сельского хозяйства и местного производства продуктов.",
    "Инвестирование в технологии улавливания углерода.",
    "Образование и повышение осведомленности о проблемах изменения климата.",
    "Участие в экологических акциях и поддержка организаций, борющихся с изменением климата."
]
photos = [
    'https://media.istockphoto.com/id/1477849066/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B7%D0%B0%D1%81%D1%83%D1%85%D0%B0-%D0%B8-%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9-%D0%BA%D1%80%D0%B8%D0%B7%D0%B8%D1%81.jpg?s=612x612&w=0&k=20&c=aeNfh_Vh9VvLTiRtW_flmaxa8nIrETRXnfW0cthF5WA=',
    'https://media.istockphoto.com/id/1333718098/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BB%D0%B5%D1%81%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D0%B6%D0%B0%D1%80%D1%8B-%D0%B2%D1%8B%D0%B7%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BA%D0%BB%D0%B8%D0%BC%D0%B0%D1%82%D0%B0.jpg?s=612x612&w=0&k=20&c=NhSJhpVD1t5F-RI1C9XfBs3l1xsoEfLATpJLk-6eois=',
    'https://naked-science.ru/wp-content/uploads/2019/03/field_image_1422925463_led.jpg'
    'https://ecoportal.info/wp-content/uploads/2016/01/lednik-grinell.jpg'
    'https://otvet.imgsmail.ru/download/20529434_46d31f14e5e1f7ff8fd52b8b7f8affe5_800.jpg'
    'https://naked-science.ru/wp-content/uploads/2018/07/field_image_ct-climate-change-report-20171030.jpg'
    'https://www.inesnet.ru/wp-content/uploads/2022/06/img08062022.jpg'
    'https://avatars.dzeninfra.ru/get-zen_doc/1945957/pub_61519ff3eebd2f01458c7445_6151a3f41cb63d43ace6154f/scale_1200'
]
@bot.message_handler(commands=['save'])
def send_random_way(message):
    save = random.choice(save_earth)
    bot.reply_to(message, save)

@bot.message_handler(commands=['facts'])
def send_facts(message):
    facts = random.choice(global_warming_facts)
    bot.reply_to(message, facts)

@bot.message_handler(commands=['reasons'])
def send_random_reason(message):
    reason = random.choice(global_warming_reasons)
    bot.reply_to(message, reason)

@bot.message_handler(commands=['photo'])
def send_random_photo(message):
    image_url = random.choice(photos)
    bot.send_photo(message.chat.id, image_url)

# Запускаем бота
bot.polling()