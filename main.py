import json
from datetime import date, timedelta
import requests
import telebot
from telebot import types
import pygeos
from config import token, APPID
#new raw

bot = telebot.TeleBot(token)
api_url = 'http://api.openweathermap.org/data/2.5/weather'
spisok_gorodov = json.load(open('db/data_01.json', 'r', encoding='utf-8'))# загрузка из файл
today = date.today()# год месяц число
month = date.today().month# число месяца
current_day = today.day# число дня сегодня
yesterday = date.today() + timedelta(days=1)# год месяц число на завтра
current_yester_day = yesterday.day# число дня на завтра
data = [month, current_day, current_yester_day]
# def name_month():
#     if data[0] == 1:
#         return 'Января'
#     elif data[0] == 2:
#         return 'Февраля'
# print(name_month())
z = list(spisok_gorodov.values())
for i, (key, value) in enumerate(spisok_gorodov .items()):
    res = requests.get(api_url, params=z[i])
    data = res.json()
    town ='Текущая температура в городе {}   {}, ощущается как {}  сегодня {}. Скорость ветра {}'.format(z[i]['city'], data["main"]["temp"], data["main"]["feels_like"],today,data['wind']['speed'])
    if i == 0:
        template_city = town
    elif i == 1:
        template_city1 = town
    elif i == 2:
        template_city2 = town
    elif i == 3:
        template_city3 = town
    elif i == 4:
        template_city4 = town
    print(town)

# @bot.message_handler(func= lambda message:True)
# def main_handler(message):
#     user_id = str(message.from_user.id)
#     if message.text == '/start':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add(types.KeyboardButton("Погода"))
#         bot.send_message(
#             user_id,
#             'Этот бот подсказывет погоду',
#             reply_markup=markup
#         )
#     elif message.text == 'Погода':
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # markup.add(
    #     *[types.KeyboardButton(button) for button in ['Бованенково', 'Харасавэй']])
    # bot.send_message(user_id, 'Выберите город:', reply_markup=markup)
    #     keyboard = types.InlineKeyboardMarkup()
    #     callback_button = types.InlineKeyboardButton(text="Бованенково", callback_data="test")
    #     callback_button1 = types.InlineKeyboardButton(text="Харасавэй", callback_data="test1")
    #     callback_button2 = types.InlineKeyboardButton(text="Новый Уренгой", callback_data="test2")
    #     callback_button3 = types.InlineKeyboardButton(text="Омск", callback_data="test3")
    #     callback_button4 = types.InlineKeyboardButton(text="Уфа", callback_data="test4")
    #array = ['Hello', 'Goodbye', 'Start', 'Price']
    #keyboard.add(*array)
    #keyboard.add(callback_button3, )
        # keyboard.add(callback_button, callback_button1, callback_button3, row_width=2)
        # keyboard.row(callback_button2, callback_button4)
        #
        # bot.send_message(user_id, "Выберите город:", reply_markup=keyboard)

# @bot.message_handler(content_types=['text'])
# def pogoda(message):
#     if message.text == "Бованенково":
#         bot.send_message(message.from_user.id, city = weather.city)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):

    # if call.message:
    #     if call.data == "test":
    #         bot.send_message(chat_id=call.message.chat.id, text=template_city)
    #     elif call.data == "test1":
    #         bot.send_message(chat_id=call.message.chat.id, text=template_city1)
    #     elif call.data == "test2":
    #         bot.send_message(chat_id=call.message.chat.id, text=template_city2)
    #     elif call.data == "test3":
    #         bot.send_message(chat_id=call.message.chat.id, text=template_city3)
    #     elif call.data == "test4":
    #         bot.send_message(chat_id=call.message.chat.id, text=template_city4)


#json.dump(data, open('db/data_01.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)#выгрузка в файл
#print(res.json())

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
