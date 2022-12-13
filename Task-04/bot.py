import os
import telebot
import requests
import json
import csv

os.environ['Api_key'] = '730c2794'
os.environ['id_bot'] = '5817756447:AAHvLQaQXk2awJ7LLxzCnY_od6WyEZzQ2J0'


# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('Api_key')
bot_id = os.getenv('id_bot')

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    
    bot.reply_to(message, 'Getting movie info...')  
    
    # TODO: 1.2 Get movie information from the API
    movie_name = message.text[7:]                      #getting movie from telegram chat
    APIKEY = '730c2794'                                #apikey for url
    response = requests.get('http://www.omdbapi.com/?t=' + movie_name + '&apikey=' + APIKEY).json()
    movie = response['Title']
    poster = response['Poster']
    year = response['Year']
    released = response['Released']
    imdbRating = response['imdbRating']

    # TODO: 1.3 Show the movie information in the chat window
    bot.send_message(message.chat.id, 'Movie found!')
    bot.send_message(message.chat.id, poster)
    bot.send_message(message.chat.id, 'Movie Name - ' + movie)
    bot.send_message(message.chat.id, 'Year - ' + year)
    bot.send_message(message.chat.id, 'Released - ' + released)
    bot.send_message(message.chat.id, 'IMDB Rating - ' + imdbRating)

    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open('movie.csv', 'w', newline='') as f1:
        writer = csv.writer(f1, delimiter=' ')
        header = ['Movie Name', 'Year', 'Released', 'IMDB Rating']
        writer.writerow(header)
        data = [movie, year, released, imdbRating]
        writer.writerow(data)

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

    #TODO: 2.2 Send downlodable CSV file to telegram chat
    movie_file = open('movie.csv', 'r')
    bot.send_document(message.chat.id, movie_file)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
