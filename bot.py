from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from datetime import *
import logging
import settings


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
    updater.start_polling()
    updater.idle()

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

def get_planet_name(command):
    command_list = command.split()
    if len(command_list) > 1:
        return command_list[1]
    else:
        return ""



    return command.split()[1]

def get_constellation (planet_name):
    planets = {
    "Mercury":ephem.Mercury,
    "Venus":ephem.Venus,
    "Mars":ephem.Mars,
    "Jupiter":ephem.Jupiter,
    "Saturn":ephem.Saturn,
    "Uranus":ephem.Uranus,
    "Neptune":ephem.Neptune,
    "Pluto":ephem.Pluto,
    "Moon":ephem.Moon,
    }

    if planet_name in planets:
        planet = planets[planet_name](datetime.today())
        return ephem.constellation(planet)[1]
    else:
        return "Такой планеты в нашем космосе нет: " + planet_name

if __name__ == "__main__":
   main()