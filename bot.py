from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import ephem
from datetime import *
import logging
import settings
import re
import operator
import russiancities

cities = list(russiancities.russian_cities)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
    )


current_question_num = 0

greeting_text = """Добрый день, {}! Я чатбот-астроном. Спросите про планету командой /planet"""


def main():

    updater = Updater(settings.TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_planet))
    dp.add_handler(CommandHandler("wordcount", word_count))    
    dp.add_handler(CommandHandler("calc", calc))    

    text_handler = MessageHandler(Filters.text, handle_text)
    dp.add_handler(text_handler)     # без регистрации будет работать, 

    dp.add_handler(CommandHandler("calc", calc))    

    updater.start_polling()
    updater.idle()


def handle_text(bot, update):

    text = update.message.text.lower()

    command = "когда ближайшее полнолуние после"

    my_date = ""
    if text[0:len(command)] == command:
        my_date = text[len(command)+1:]
        try:
            update.message.reply_text(str(ephem.next_full_moon(my_date)))
        except ValueError:
            update.message.reply_text("Какая-то странная дата: " + my_date)

    # playing cities game
    input_city = update.message.text
    print ("количество городов " + str(len(cities)))
    if input_city in cities:
        # This is our city
        last_letter = input_city[-1]
        for city in cities:
            if city[:1].lower() == last_letter:
                update.message.reply_text(city + ", ваш ход")
                cities.remove(input_city)
                cities.remove(city)
                return
                

def greet_user(bot, update):
    replay_back_text = greeting_text.format(update.message.chat.first_name)
    logging.info("Bot started")
    update.message.reply_text(replay_back_text)

def find_planet(bot, update):
    planet_name = get_planet_name(update.message.text)
    if planet_name == "":
        logging.info("Wrong format")
        update.message.reply_text('Пример использования команды: "/planet Mars"')
        return
    replay_back_text = get_constellation(planet_name)
    logging.info("Found planet")
    update.message.reply_text(replay_back_text)

def word_count(bot, update):
    text = get_command_text(update.message.text)
    words = re.split("[ .,;@#$%^&*(){}|?~]", text)
    update.message.reply_text(len(words))    

def calc(bot, update):
    input_text = get_command_text(update.message.text)

    if input_text.lower() == "/calc":
        calc_keyboard = [['1', '2', '3'], 
        ['4', '5', '6'], 
        ['7', '8', '9'],
        ['0', '+', '-'],
        ['*', '/', '=']]

        reply_markup = telegram.ReplyKeyboardMarkup(calc_keyboard)
        bot.send_message(chat_id=update.message.chat_id, 
            text="Calculator", 
            reply_markup=reply_markup)

    # working on text expressions
    command_skolko = "сколько будет"

    text_expression = ""

    if input_text[0:len(command_skolko)].lower() == command_skolko:
        text_expression = input_text[len(command_skolko)+1:]
        expression_dic = {
            "один": "1",    
            "два": "2",    
            "три": "3",    
            "четыре": "4",    
            "пять": "5",    
            "шесть": "6",    
            "семь": "7",    
            "восемь": "8",    
            "девять": "9",    
            "ноль": "0",    
            "плюс": "+",    
            "минус": "-",    
            "умножить": "*",    
            "разделить": "/",
            "и": "."
        }
        for i in expression_dic:
            text_expression = text_expression.replace(i, expression_dic[i])
        text_expression = text_expression.replace(" ", "")    
        input_text = text_expression + "="



    if input_text[-1] != "=":
        update.message.reply_text("Expression should end with '='")         
        return
    text = input_text[0:-1]

    # Split into arithmetical operations
    calc_array = re.split("[\+\-*/]", text)

    if len(calc_array)!=2:
        update.message.reply_text("Expression should look like 2+3=")
        return

    m = re.search("[\+\-*/]", text)
    operation = m.group(0)


    # calculate operation
    operations = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv
             }

    try:
        result = operations[operation](float(calc_array[0]), float(calc_array[1]))
    except ZeroDivisionError:
        update.message.reply_text("Деление на ноль")
        return
    except ValueError:
        update.message.reply_text("Expression should look like 2+3=")
        return


    update.message.reply_text(input_text + str(result))    


def get_planet_name(command):
    command_list = command.split()
    if len(command_list) > 1:
        return command_list[1]
    else:
        return ""

def get_command_text(command):
    i = command.find(" ")+1
    return command[i:]

def get_constellation (planet_name):
    planets = {
    "Mercury": ephem.Mercury,
    "Venus": ephem.Venus,
    "Mars": ephem.Mars,
    "Jupiter": ephem.Jupiter,
    "Saturn": ephem.Saturn,
    "Uranus": ephem.Uranus,
    "Neptune": ephem.Neptune,
    "Pluto": ephem.Pluto,
    "Moon": ephem.Moon,
    }

    if planet_name in planets:
        planet = planets[planet_name](datetime.today())
        return ephem.constellation(planet)[1]
    else:
        return "Такой планеты в нашем космосе нет: " + planet_name

if __name__ == "__main__":
   main()