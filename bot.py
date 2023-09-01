# -- coding: utf-8 --

from telebot import TeleBot
import csv
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from enviaremail import CriandoEmail

BOT_TOKEN = '<INSIRA O TOKEN DO SEU BOT AQUI>'

bot = TeleBot(BOT_TOKEN, parse_mode='HTML')

criar_email = CriandoEmail()

#SALVAR dados da conversa com o chatbot em arquivos csv
def salvar(arquivo, conversa: list):
    chat = open(arquivo,'a', encoding="utf-8")
    e = csv.writer(chat)
    e.writerow(conversa)


@bot.message_handler(commands=['start'])
def send_start(message):
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('💻 Canais', callback_data='canais'),
               InlineKeyboardButton('🤑 Doação', callback_data='doacao'))
    markup.add(InlineKeyboardButton('😎 Admin', url='https://t.me/ordnavile'))
    bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    bot.send_message(chat_id, '🤖 Explorer Bot 🤖', reply_markup=markup)
    bot.delete_message(chat_id, message_id=message.message_id)
    conversa = [
            datetime.now().strftime('%d/%m/%Y %H:%M:%S'), # data e hora do envio
            message.chat.id, # ID do chat
            message.from_user.username, # nome do usuário que enviou o arquivo
            message.content_type, # tipo do arquivo enviado
            message.text
        ]
    salvar('clientes.csv', conversa)
    criar_email.enviando_email()


@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    message_id = message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
    bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    bot.send_message(chat_id, """ Quer inserir seu canal ou grupo no catálogo?
Envei uma DM para @ordnavile com o link do seu grupo ou canal, é gratuito e sempre será!😉
        """, reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document',
                                                               'text', 'location', 'contact', 'sticker', 'animation'])
def default_command(message):
    if message.content_type == message.content_type:
        bot.send_chat_action(chat_id=message.from_user.id, action='typing')
        bot.send_message(message.chat.id, """Não é um comando válido.😕
Digite /start para interagir com o bot.🤖""")
        bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'doacao')
def callback_valores(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
        
    chave_pix = '1c60cdac-4a1e-4146-a141-c1329f487615 \n\n Faça uma doação!😉'

    image_file = open('pix.jpeg', 'rb')
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Retornar', callback_data='start'))
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.send_photo(chat_id, image_file, caption=chave_pix, reply_markup=markup)
    bot.edit_message_reply_markup(chat_id, message_id)
     

@bot.callback_query_handler(func=lambda call: call.data == 'canais')
def callback_canais(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('🎵 Músicas', callback_data='musicas'),
                InlineKeyboardButton('📺 Filmes', callback_data='filmes'),
                InlineKeyboardButton('🗞 Notícias', callback_data='noticias'),
                InlineKeyboardButton('🌎 Mundo', callback_data='mundo'),
                # InlineKeyboardButton('🗿 RedPill', callback_data='redpill'),
                InlineKeyboardButton('💻 Tecnologia', callback_data='tecnologia'),
                InlineKeyboardButton('📚 Cursos', callback_data='cursos'),
                InlineKeyboardButton('🔡 Idiomas', callback_data='idiomas'),
                InlineKeyboardButton('🕹 Games', url='https://t.me/gamee'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'musicas')
def callback_musicas(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton('🎤 Rap', callback_data='rap'),
                InlineKeyboardButton('🪘 Pagode', callback_data='pagode'),
                InlineKeyboardButton('🔊 Funk', callback_data='funk'),
                InlineKeyboardButton('🎸 Rock', callback_data='rock'),
                InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                InlineKeyboardButton('🎷 Blues', callback_data='blues'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rap')
def callback_rap(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎤 Racionais Mc's", url='https://t.me/musicaracionaismcs'),
                InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/musicasrapnacional'),
                InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'pagode')
def callback_pagode(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🪘  Pagode do Bom", url='https://t.me/Pagodes1600Misturados'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'funk')
def callback_funk(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🔊 Fluxo do Funk", url='https://t.me/Aaaaabcrd'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rock')
def callback_rock(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎸 Rock Som das Antigas", url='https://t.me/somdasantigas'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'blues')
def callback_blues(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎷 Blues Music Relaxing", url='https://t.me/songblues'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'jazz')
def callback_jazz(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎹 Jazz Music Relaxing", url='https://t.me/songjazz'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'filmes')
def callback_filmes(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton('📺 Filmes Arte', url='https://t.me/FilmsArte'),
                InlineKeyboardButton('📺 Testosterona', url='https://t.me/Testosteronaa'),
                InlineKeyboardButton('📺 TopFlix', url='https://t.me/TopFlixx_Bot'),
                InlineKeyboardButton('📺 Filmes Policiais', url='https://t.me/cineminhapolicial'),
                InlineKeyboardButton('📺 Filmes e Séries', url='https://t.me/filmes'),
                InlineKeyboardButton('📺 Filmes | Series | Horoscopo', url='https://t.me/filmes_atores'))
    markup.add(InlineKeyboardButton('🔞 Adulto', callback_data='adulto'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'adulto')
def callback_adulto(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🔞 Amadoras BR", url='https://t.me/amadorasbrcaiunaneteafins'),
                InlineKeyboardButton('🔞 Machismo Realista', url='https://t.me/MachismoRealistaAbsoluto'),
                InlineKeyboardButton('🔞 Wheyfus', url='https://t.me/wheyfus'),
                InlineKeyboardButton('🔞Macetava?', url='https://t.me/macetavakkk'),
                InlineKeyboardButton('🔞 Comedores de Preta', url='https://t.me/ComedordePreta'),
                InlineKeyboardButton('🔞 Revista +18', url='https://t.me/+xZof5dnNZpY5ZDFh'),
                InlineKeyboardButton('🔞 OnlyFans Content', url='https://t.me/+AvrCcQEL4OIyOTlh'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='filmes'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'noticias')
def callback_noticias(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🗞 Tupi Report", url='https://t.me/tupireport'),
                InlineKeyboardButton('🗞 InfoMoney', url='https://t.me/infomoney_noticias'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'mundo')
def callback_mundo(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🌎 Live Leak", url='https://t.me/leaklive'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'tecnologia')
def callback_tec(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("📱 Termux Hacker ", url='https://t.me/Termux_For_Android'))
    markup.add(InlineKeyboardButton("📱 Termux Hacking Commands ", url='https://t.me/Termux_Hacking_TLS'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'cursos')
def callback_cursos(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("📚 Learn Ethical Hacking", url='https://t.me/wh8teHatHacking'),
                InlineKeyboardButton('💻 DevWorld - Cursos', url='https://t.me/DevWorldCursosBot'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'idiomas')
def callback_idiomas(call):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglês 🏴󠁧󠁢󠁥󠁮󠁧󠁿', url='https://t.me/inglespelotelegram'),
                InlineKeyboardButton('🇪🇸 Espanhol 🇪🇸', url='https://t.me/espanholcombeta'),
                InlineKeyboardButton('🇫🇷 Francês 🇫🇷', url='https://t.me/francesmairovergara'),
                InlineKeyboardButton('🇩🇪 Alemão 🇩🇪', url='https://t.me/Cursoalemao'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def callback_start(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id)
    send_start(call.message) # chama a função send_start novamente para mostrar o menu inicial
    bot.answer_callback_query(callback_query_id=call.id, text='Opção inválida. Tente novamente.')


if __name__ == '__main__':
    print('Bot running...')
    bot.infinity_polling(skip_pending=True)
