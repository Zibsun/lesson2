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
    print (update)
    replay_back_text = greeting_text.format(update.message.chat.first_name)
    logging.info ("Bot started")
    update.message.reply_text(replay_back_text)

def find_planet(bot, update):
    print (update)
    planet_name = get_planet_name(update.message.text)
    replay_back_text = get_constellation(planet_name)
    logging.info ("Found planet")
    update.message.reply_text(replay_back_text)    

def get_planet_name(command):
    return command[7:].strip()


def get_constellation (planet_name):
    planet = ""

    if planet_name == "Mercury":
        planet = ephem.Mercury(datetime.today())
        
    if planet_name == "Venus":
        planet = ephem.Venus(datetime.today())

    if planet_name == "Mars":
        planet = ephem.Mars(datetime.today())

    if planet_name == "Jupiter":
        planet = ephem.Jupiter(datetime.today())

    if planet_name == "Saturn":
        planet = ephem.Saturn(datetime.today())

    if planet_name == "Uranus":
        planet = ephem.Uranus(datetime.today())

    if planet_name == "Neptune":
        planet = ephem.Neptune(datetime.today())

    if planet_name == "Pluto":
        planet = ephem.Pluto(datetime.today())

    if planet_name == "Moon":
        planet = ephem.Moon(datetime.today())

    if planet !="":
        return ephem.constellation(planet)[1]
    else:
        return "Failed to find " + planet_name


main()