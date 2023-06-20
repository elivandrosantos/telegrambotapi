# -- coding: utf-8 --

import telebot, csv
# import time
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# from telebot.types import ReplyKeyboardMarkup, CallbackQuery, KeyboardButton

BOT_TOKEN = 'INSIRA O TOKEN DO SEU BOT AQUI'

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')


#SALVAR dados da conversa com o chatbot em arquivos csv
def salvar (arquivo, conversa: list):
    with open(arquivo,'a') as chat:
        e = csv.writer(chat)
        e.writerow(conversa)


@bot.message_handler(commands=['start'])
def send_start(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('💻 Categorias', callback_data='categorias'),
               InlineKeyboardButton('🤑 Doação', callback_data='valores'))
    markup.add(InlineKeyboardButton('⚠️ Escola Segura', url='https://www.gov.br/mj/pt-br/escolasegura'))
    markup.add(InlineKeyboardButton('😎 Admin', url='https://t.me/ordnavile'))
    markup.add(InlineKeyboardButton('🆘 Help', callback_data='help'))
            #    InlineKeyboardButton('Some Features', callback_data='some_features'),
            #    InlineKeyboardButton('Content', callback_data='content'),
            #    InlineKeyboardButton('Quick Start', callback_data='quick_start'),
            #    InlineKeyboardButton('Types Of API', callback_data='types_of_api'),
            #    InlineKeyboardButton('Telebot Version', callback_data='telebot_version'),
            #    InlineKeyboardButton('AsyncTeleBot', callback_data='asynctelebot'),
            #    InlineKeyboardButton('Callback Data Factory', callback_data='callback_data'),
            #    InlineKeyboardButton('Utils', callback_data='utils'),
            #    InlineKeyboardButton('Formatting Options', callback_data='formatting'),
            #    InlineKeyboardButton('Help', callback_data='help'))
    # bot.send_message(chat_id, """ """, disable_web_page_preview=True)
    bot.send_message(chat_id, text=f'Olá, seja bem vindo!', reply_markup=markup)
    bot.delete_message(chat_id, message.message_id)
    # bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
#     bot.send_message(chat_id, """ Quer inserir seu canal ou grupo no catálogo?
# Envei uma DM para @ordnavile com o link do seu grupo ou canal, é gratuito e sempre será!😉
#         """)
    conversa = [
            datetime.now().strftime('%d/%m/%Y %H:%M:%S'), # data e hora do envio
            message.chat.id, # ID do chat
            message.from_user.username, # nome do usuário que enviou o arquivo
            message.content_type, # tipo do arquivo enviado
            message.text
        ]
    salvar('clicou_botao_iniciar.csv', conversa)




@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
    bot.send_message(chat_id, """ Quer inserir seu canal ou grupo no catálogo?
Envei uma DM para @ordnavile com o link do seu grupo ou canal, é gratuito e sempre será!😉
        """, reply_markup=markup)
    # bot.delete_message(chat_id, message.message_id)
    bot.delete_message(chat_id=message.from_user.id, message_id=message.message.message_id)


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document',
                                                               'text', 'location', 'contact', 'sticker', 'animation'])
def default_command(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('▶️ Start', callback_data='start'))
    markup.add(InlineKeyboardButton('🆘 Help', callback_data='help'))
#     bot.send_message(message.chat.id, """Não é um comando válido.😕
# Digite /start ou /help para interagir com o bot.🤖""", reply_markup=markup)

    if message.content_type == message.content_type:
        bot.send_chat_action(chat_id=message.from_user.id, action='typing')
        bot.send_message(message.chat.id, """Não é um comando válido.😕
Digite /start ou /help para interagir com o bot.🤖""", reply_markup=markup)
        # bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(chat_id=message.from_user.id, message_id=message.message.message_id)
        conversa = [
            datetime.now().strftime('%d/%m/%Y %H:%M:%S'), # data e hora do envio
            message.chat.id, # ID do chat
            message.from_user.username, # nome do usuário que enviou o arquivo
            message.content_type, # tipo do arquivo enviado
            message.text
        ]
        salvar('arquivos_user.csv', conversa)



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    conversa = [
        datetime.now().strftime('%d/%m/%Y %H:%M:%S'), # data e hora da mensagem
        call.message.chat.id, # ID do chat
        call.from_user.username, # nome do usuário que enviou a mensagem
        call.message.text # texto da mensagem
                ]
    # salvar('categorias.csv', conversa)


    if call.data == 'categorias':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton('📢 Canais', callback_data='canais'),
                   InlineKeyboardButton('🗣 Grupos', callback_data='grupos'),
                #    InlineKeyboardButton('🕹 Games', url='https://t.me/gamee'),
                #    InlineKeyboardButton('💻 Tecnologia', callback_data='tecnologia'),
                #     InlineKeyboardButton('Cursos', callback_data='filmes'),
                #     InlineKeyboardButton('Idiomas', callback_data='idiomas'),
                #     InlineKeyboardButton('Notícias', callback_data='noticias'),
                #     InlineKeyboardButton('RedPill', callback_data='redpill'),
                #     InlineKeyboardButton('Mundo', callback_data='mundo'),
                #     InlineKeyboardButton('Tecnologia', callback_data='tecnologia'),
                #     InlineKeyboardButton('+18', callback_data='18'),
                    # InlineKeyboardButton('🆘 Help', callback_data='help')
                    )
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start')
        )
        bot.answer_callback_query(callback_query_id=call.id)
        # bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, """ Selecione Categoria: """, reply_markup=markup)
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

        salvar('categorias.csv', conversa)



    elif call.data == 'valores':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        # salvar('valores.csv', conversa)
        chave_pix = """

1c60cdac-4a1e-4146-a141-c1329f487615

Esse projeto é 100% gratuito.
Uma coquinha e um salgado será sempre bem-vindo!😉

"""
        image_file = open('pix.jpeg', 'rb')
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Retornar', callback_data='start'))
        bot.answer_callback_query(callback_query_id=call.id)
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        bot.send_photo(chat_id, image_file, caption=chave_pix, reply_markup=markup)
        salvar('valores.csv', conversa)


    elif call.data == 'grupos':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        # markup.row_width = 2
        # markup.add(InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglês 🏴󠁧󠁢󠁥󠁮󠁧󠁿', url='https://t.me/inglespelotelegram'),
        #            InlineKeyboardButton('🇪🇸 Espanhol 🇪🇸', url='https://t.me/espanholcombeta'),
        #            InlineKeyboardButton('🇫🇷 Francês 🇫🇷', url='https://t.me/francesmairovergara'),
        #            InlineKeyboardButton('🇩🇪 Alemão 🇩🇪', url='https://t.me/Cursoalemao'),
                #    InlineKeyboardButton('◀️ Retornar', callback_data='canais'),
                #    InlineKeyboardButton('🤑 Doação', callback_data='valores'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                #    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='categorias'))
        bot.answer_callback_query(callback_query_id=call.id)
        # bot.send_message(chat_id, 'Selecione Canal Idioma:', reply_markup=markup)
        bot.send_message(chat_id,
"""Mande DM para @ordnavile para inserir seu grupo no catálogo,
é gratuito e sempre será!😎""", reply_markup=markup)
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('grupos.csv', conversa)



    elif call.data == 'canais':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('🎵 Músicas', callback_data='musicas'),
                   InlineKeyboardButton('📺 Filmes', callback_data='filmes'),
                   InlineKeyboardButton('🗞 Notícias', callback_data='noticias'),
                   InlineKeyboardButton('🌎 Mundo', callback_data='mundo'),
                   InlineKeyboardButton('🗿 RedPill', callback_data='redpill'),
                   InlineKeyboardButton('💻 Tecnologia', callback_data='tecnologia'),
                   InlineKeyboardButton('📚 Cursos', callback_data='cursos'),
                   InlineKeyboardButton('🔡 Idiomas', callback_data='idiomas'),
                   InlineKeyboardButton('🕹 Games', url='https://t.me/gamee'),
                   )
        # markup.add(InlineKeyboardButton('🕹 Games', url='https://t.me/gamee'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='categorias'))
        bot.send_message(chat_id, 'Selecione o Canal', reply_markup=markup)
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('canais.csv', conversa)


    elif call.data == 'musicas':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(InlineKeyboardButton('🎤 Rap', callback_data='rap'),
                    InlineKeyboardButton('🪘 Pagode', callback_data='pagode'),
                    InlineKeyboardButton('🔊 Funk', callback_data='funk'),
                    InlineKeyboardButton('🎸 Rock', callback_data='rock'),
                    InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                   InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('musicas.csv', conversa)



    elif call.data == 'rap':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🎤 Racionais Mc's", url='https://t.me/musicaracionaismcs'),
                   InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                    InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                    InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal de Rap:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('rap.csv', conversa)


    elif call.data == 'pagode':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🪘  Pagode do Bom", url='https://t.me/Pagodes1600Misturados'),
                #    InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                #     InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                #     InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas Rap:', reply_markup=markup)
       # bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('pagode.csv', conversa)


    elif call.data == 'funk':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🔊 Fluxo do Funk", url='https://t.me/Aaaaabcrd'),
                #    InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                #     InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                #     InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas Rap:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('funk.csv', conversa)


    elif call.data == 'rock':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🎸 Rock Som das Antigas", url='https://t.me/somdasantigas'),
                #    InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                #     InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                #     InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas Rap:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('rock.csv', conversa)




    elif call.data == 'blues':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🎷 Blues Music Relaxing", url='https://t.me/songblues'),
                #    InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                #     InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                #     InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas Rap:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('blues.csv', conversa)



    elif call.data == 'jazz':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🎹 Jazz Music Relaxing", url='https://t.me/songjazz'),
                #    InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                #     InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                #     InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'),
                #     InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🎷 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Músicas Rap:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('jazz.csv', conversa)



    elif call.data == 'filmes':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 3
        markup.add(InlineKeyboardButton('📺 Filmes Arte', url='https://t.me/FilmsArte'),
                    InlineKeyboardButton('📺 Testosterona', url='https://t.me/Testosteronaa'),
                    InlineKeyboardButton('📺 TopFlix', url='https://t.me/TopFlixx_Bot'),
                    InlineKeyboardButton('📺 Filmes Policiais', url='https://t.me/cineminhapolicial'),
                    InlineKeyboardButton('📺 Filmes e Séries', url='https://t.me/filmes'),
                   InlineKeyboardButton('📺 Filmes | Series | Horoscopo', url='https://t.me/filmes_atores'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )
        markup.add(InlineKeyboardButton('🔞 Adulto', callback_data='adulto'))
        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal de Filme:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('filmes.csv', conversa)



    elif call.data == 'noticias':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🗞 Tupi Report", url='https://t.me/tupireport'),
                   InlineKeyboardButton('🗞 InfoMoney', url='https://t.me/infomoney_noticias'),
                    # InlineKeyboardButton('🗞 Wheyfus', url='https://t.me/wheyfus'),
                    # InlineKeyboardButton('🗞Macetava?', url='https://t.me/macetavakkk'),
                #     InlineKeyboardButton('🗞 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🗞 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Notícias:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('noticias.csv', conversa)


    elif call.data == 'mundo':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🌎 Live Leak", url='https://t.me/leaklive'),
                #    InlineKeyboardButton('🌎 InfoMoney', url='https://t.me/infomoney_noticias'),
                    # InlineKeyboardButton('🌎 Wheyfus', url='https://t.me/wheyfus'),
                    # InlineKeyboardButton('🌎Macetava?', url='https://t.me/macetavakkk'),
                #     InlineKeyboardButton('🌎 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🌎 Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Notícias:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('mundo.csv', conversa)


    elif call.data == 'redpill':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🗿 Projeto Conselho", url='https://t.me/projetoconselho'),
                #    InlineKeyboardButton('🗿 InfoMoney', url='https://t.me/infomoney_noticias'),
                    # InlineKeyboardButton('🗿 Wheyfus', url='https://t.me/wheyfus'),
                    # InlineKeyboardButton('🗿Macetava?', url='https://t.me/macetavakkk'),
                #     InlineKeyboardButton('🗿 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('🗿Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal RedPill:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('redpill.csv', conversa)



    elif call.data == 'tecnologia':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("💻 InNovTech ", url='https://t.me/AYZAKIEL_4'),
                    # InlineKeyboardButton('💻 DevWorld - Cursos', url='https://t.me/DevWorldCursosBot'),
                    # InlineKeyboardButton('💻 Wheyfus', url='https://t.me/wheyfus'),
                    # InlineKeyboardButton('💻Macetava?', url='https://t.me/macetavakkk'),
                #     InlineKeyboardButton('💻 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('💻Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Tecnologia:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('tecnologia.csv', conversa)


    elif call.data == 'cursos':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("📚 Culto de Toth ", url='https://t.me/+GMz2F8SVyNsxMDcx'),
                    InlineKeyboardButton('💻 DevWorld - Cursos', url='https://t.me/DevWorldCursosBot'),
                #    InlineKeyboardButton('📚 InfoMoney', url='https://t.me/infomoney_noticias'),
                    # InlineKeyboardButton('📚 Wheyfus', url='https://t.me/wheyfus'),
                    # InlineKeyboardButton('📚Macetava?', url='https://t.me/macetavakkk'),
                #     InlineKeyboardButton('📚 Jazz', callback_data='jazz'),
                #    InlineKeyboardButton('📚Blues', callback_data='blues'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Cursos:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('cursos.csv', conversa)



    elif call.data == 'adulto':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("🔞 Amadoras BR", url='https://t.me/amadorasbrcaiunaneteafins'),
                   InlineKeyboardButton('🔞 Machismo Realista', url='https://t.me/MachismoRealistaAbsoluto'),
                    InlineKeyboardButton('🔞 Wheyfus', url='https://t.me/wheyfus'),
                    InlineKeyboardButton('🔞Macetava?', url='https://t.me/macetavakkk'),
                    InlineKeyboardButton('🔞 Live18Funk', url='https://t.me/lives18funk'),
                   InlineKeyboardButton('🔞 Revista +18', url='https://t.me/+xZof5dnNZpY5ZDFh'),
                   InlineKeyboardButton('🔞 OnlyFans Content', url='https://t.me/+AvrCcQEL4OIyOTlh'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                    )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='filmes'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Adulto:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('adulto.csv', conversa)



    elif call.data == 'idiomas':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglês 🏴󠁧󠁢󠁥󠁮󠁧󠁿', url='https://t.me/inglespelotelegram'),
                   InlineKeyboardButton('🇪🇸 Espanhol 🇪🇸', url='https://t.me/espanholcombeta'),
                   InlineKeyboardButton('🇫🇷 Francês 🇫🇷', url='https://t.me/francesmairovergara'),
                   InlineKeyboardButton('🇩🇪 Alemão 🇩🇪', url='https://t.me/Cursoalemao'),
                #    InlineKeyboardButton('◀️ Retornar', callback_data='canais'),
                #    InlineKeyboardButton('🤑 Doação', callback_data='valores'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram'),
                #    InlineKeyboardButton('Inglês Pelo Telegram', url='https://t.me/inglespelotelegram')
                   )

        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, 'Selecione Canal Idioma:', reply_markup=markup)
        #bot.send_message(chat_id, 'Mande DM para @ordnavile para inserir seu grupo ou canal no catálogo, é gratuito e sempre será!😎')
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        salvar('idiomas.csv', conversa)



    elif call.data == 'help':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('🤑 Doação', callback_data='valores'))
        markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(chat_id, """ Quer inserir seu canal ou grupo no catálogo?
Envei uma DM para @ordnavile com o link do seu grupo ou canal, é gratuito e sempre será!😉
        """, reply_markup=markup)
        # bot.delete_message(chat_id, message_id)
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)



    elif call.data == 'start':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.answer_callback_query(callback_query_id=call.id)
        send_start(call.message) # chama a função send_start novamente para mostrar o menu inicial


    else:
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.answer_callback_query(callback_query_id=call.id, text='Opção inválida. Tente novamente.')


if __name__ == '__main__':
    print('Bot running...')
    bot.infinity_polling(skip_pending=True)
