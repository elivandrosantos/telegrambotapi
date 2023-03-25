# -- coding: utf-8 --

import telebot
from telebot.util import antiflood
import time
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# from telebot.service_utils import quick_markup


API_TOKEN = '<seu token>'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def receiving_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, """
Welcome to pyTelegramBotAPI’s documentation!
Bot created by Elivandro Santos, 
this project is part of the learning path of reading 
pyTelegramBotAPI’s 4.9.0 documentation.

Intent is only for learning and helping other beginners
to read this simple and easy learning documentation, not for sale.

GitHub: https://github.com/elivandrosantos

E-mail: elivandrocsantos@gmail.com

Send DM Telegram: @ordnavile""", disable_web_page_preview=True)

    menu_options = [
        '/telebot - Description',
        '/chats - Chat List',
        '/some_features - Some features',
        '/content - Content',
        '/quick_start - Quick Start',
        '/types_of_api - Types of API',
        '/telebot_version - TeleBot Version',
        '/asynctelebot - AsyncTeleBot',
        '/callback_data_factory - Callback Data Factory',
        '/utils - Utils',
        '/formatting_options - Formatting Options',
        '/help - Help'
    ]
    menu_text = '⚠️ MAIN MENU ⚠️\n\n' + '\n'.join(menu_options)
    bot.reply_to(message, menu_text)

    msg = antiflood(bot.send_message, chat_id,  """⚠️Watch out for the flood!⚠️
Send messages every few seconds to avoid blocking the bot.""", time.sleep(1))

   
    

        

@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Questions about bot functionality, send an email to elivandrocsantos@gmail.com or telegram @ordnavile\n' \
                     '\n' \
                     'MAIN MENU: /start')
    
    
    
    



@bot.message_handler(commands=['telebot'])
def receiving_telebot(message):
    chat_id = message.chat.id
    url = 'https://core.telegram.org/bots/api'
    bot.reply_to(message, f'TeleBot is synchronous and asynchronous implementation of Telegram Bot API\n{url}\n' \
                          f'\n' \
                          f'RETURN /start' 
                )


@bot.message_handler(commands=['chats'])
def receiving_chats(message):
    chat_id = message.chat.id
    chat_telegram = 'https://telegram.me/joinchat/Bn4ixj84FIZVkwhk2jag6A'
    chat_russo = 'https://t.me/pytelegrambotapi_talks_ru'
    chat_noticias = 'https://t.me/pytelegrambotapi'
    baixando_pypi = 'https://pypi.org/project/pyTelegramBotAPI/'
    repositorio_github = 'https://github.com/eternnoir/pyTelegramBotAPI'

    url_chat = f'English chat: {chat_telegram}\n ' \
               f'\n' \
               f'Russian chat: {chat_russo}\n' \
               f'\n' \
               f'News: {chat_noticias}\n' \
               f'\n' \
               f'Pypi: {baixando_pypi} \n ' \
               f'\n' \
               f'Source:: Github repository {repositorio_github}\n' \
               f'\n' \
               f'RETURN /start' 
    bot.reply_to(message, f'{url_chat}', disable_web_page_preview=True)




@bot.message_handler(commands=['some_features'])
def receiving_some(message):
    chat_id = message.chat.id
    msg_help = bot.reply_to(message, 'Easy to learn and use.\n'
                                     'Easy to understand.\n'
                                     'Both sync and async.\n'
                                     'Examples on features.\n'
                                     'States\n'
                                     'And more…\n'
                                     '\n'
                                     'RETURN /start' 
                            )
    

@bot.message_handler(commands=['content'])
def receiving_content(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Enter options in menu\n' \
                     '\n' \
                     'Instalation Guide: /installation_guide \n' \
                                     'Using PIP: /using_pip \n' \
                                     'Usingi pipenv: /using_pipenv \n'\
                                     'By Cloning Repositoy: /by_cloning_repository \n' \
                                     'Directly Using pip: /directly_using_pip \n' \
                                     '\n' \
                                     'RETURN /start'
                                     
                            )
    


@bot.message_handler(commands=['installation_guide'])
def receiving_guide(message):
    chat_id = message.chat.id
    url_guide = 'https://pytba.readthedocs.io/en/latest/install.html\n' \
                '\n' \
                'MAIN MENU: /start\n' \
                'RETURN: /content'
    with open('guide.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_guide)



@bot.message_handler(commands=['using_pip'])
def receiving_pip(message):
    chat_id = message.chat.id
    url_pip = 'https://pytba.readthedocs.io/en/latest/install.html#using-pip\n' \
              '\n' \
              'MAIN MENU: /start\n' \
              'RETURN: /content'
    with open('using_pip.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_pip)



@bot.message_handler(commands=['using_pipenv'])
def receiving_pipenv(message):
    chat_id = message.chat.id
    url_pipenv = 'https://pytba.readthedocs.io/en/latest/install.html#using-pipenv\n' \
                 '\n' \
                 'MAIN MENU: /start\n' \
                 'RETURN: /content'
    with open('using_pipenv.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_pipenv)



@bot.message_handler(commands=['by_cloning_repository'])
def receiving_cloning_repository(message):
    chat_id = message.chat.id
    url_cloning_repository = 'https://pytba.readthedocs.io/en/latest/install.html#by-cloning-repository\n' \
                             '\n' \
                             'MAIN MENU: /start\n' \
                             'RETURN: /content'
    with open('by_cloning_repository.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_cloning_repository)



@bot.message_handler(commands=['directly_using_pip'])
def receiving_directly_using_pip(message):
    chat_id = message.chat.id
    url_directly_using_pip = 'https://pytba.readthedocs.io/en/latest/install.html#directly-using-pip\n' \
                             '\n' \
                             'MAIN MENU: /start\n' \
                             'RETURN: /content'
    with open('directly_using_pip.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_directly_using_pip)



@bot.message_handler(commands=['quick_start'])
def receiving_quick_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Enter options in menu\n' \
                              '\n' \
                              'Synchronous TeleBot: /synchronous_telebot \n' \
                              '\n'
                              'Asynchronous TeleBot: /asynchronous_telebot \n' \
                              '\n' \
                              'RETURN: /start'
                            
                    )


@bot.message_handler(commands=['synchronous_telebot'])
def receiving_synchronous_telebot(message):
    chat_id = message.chat.id
    url_synchronous_telebot = 'https://pytba.readthedocs.io/en/latest/quick_start.html#synchronous-telebot\n' \
                              '\n' \
                              'MAIN MENU: /start\n' \
                              'RETURN: /quick_start'
                              
    with open('synchronous_telebot.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_synchronous_telebot)
        


@bot.message_handler(commands=['asynchronous_telebot'])
def receiving_asynchronous_telebot(message):
    chat_id = message.chat.id
    url_asynchronous_telebot = 'https://pytba.readthedocs.io/en/latest/quick_start.html#asynchronous-telebot\n' \
                               '\n' \
                               'MAIN MENU: /start\n' \
                               'RETURN: /quick_start'
                               
    with open('asynchronous_telebot.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_asynchronous_telebot)
        

@bot.message_handler(commands=['types_of_api'])
def receiving_types_of_api(message):
    chat_id = message.chat.id
    url_types_of_api = 'Needs an in-depth reading\n\n' \
                       'https://pytba.readthedocs.io/en/latest/types.html\n' \
                       '\n' \
                       'MAIN MENU: /start\n' \

    with open('types_of_api.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_types_of_api)


@bot.message_handler(commands=['telebot_version'])
def receiving_telebot_version(message):
    chat_id = message.chat.id
    url_telebot_version = 'Needs an in-depth reading\n\n' \
    'https://pytba.readthedocs.io/en/latest/sync_version/index.html\n' \
                '\n' \
                'MAIN MENU: /start\n' \

    with open('TeleBot_Version.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_telebot_version)


@bot.message_handler(commands=['asynctelebot'])
def receiving_asynctelebot(message):
    chat_id = message.chat.id
    url_asynctelebot = 'https://pytba.readthedocs.io/en/latest/async_version/index.html\n' \
                  '\n' \
                  'MAIN MENU: /start\n' \

    with open('AsyncTeleBot.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_asynctelebot)


@bot.message_handler(commands=['callback_data_factory'])
def receiving_callback_data_factory(message):
    chat_id = message.chat.id
    url_callback_data_factory = """
    

https://pytba.readthedocs.io/en/latest/calldata.html

MAIN MENU: /start
"""
    with open('callback_data_factory.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_callback_data_factory)


@bot.message_handler(commands=['utils'])
def receiving_utils(message):
    chat_id = message.chat.id
    url_utils = """
https://pytba.readthedocs.io/en/latest/util.html

MAIN MENU: /start
"""
    with open('utils.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_utils)


@bot.message_handler(commands=['formatting_options'])
def receiving_formatting_options(message):
    chat_id = message.chat.id
    url_formatting_options = """
https://pytba.readthedocs.io/en/latest/util.html

MAIN MENU: /start
"""
    with open('formatting_options.png', 'rb') as image_file:
        bot.send_photo(chat_id, image_file, caption=url_formatting_options)


    

bot.infinity_polling(skip_pending=True)

