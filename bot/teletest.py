# -*- coding: utf-8 -*-

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
# from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto
# import asyn
# from pprint import pprint
# import time
# from multiprocessing import Process, Pool
# import psycopg2




bot = telepot.Bot('123506925:AAGo1KwBgf7qb24EpyZtxzQdbC-pRtJIfN8')

def handle(msg):
    # print msg
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id
bot.notifyOnMessage(handle)
# def send_message(resp):
#     user_id = resp['message']['from']['id']
#     text = resp['message']['text']
#     bot.sendMessage(user_id, text)
    # if(text == u"Пидор"):
    #     bot.sendMessage(user_id, u"Сам пидор")
    # else:
    #     bot.sendMessage(user_id, text)
# while i!=0:
#
#     response = bot.getUpdates()
#
#
#     process_number = len(response)
#     if process_number != 0:
#
#         # pool = Pool(processes=process_number)
#
#         # print len(response)
#
#
#
#             # bot.setWebhook()
#         # bot.notifyOnMessage(handle)
#         for i in range(process_number):
#             info = bot.getMe()
#             resp = []
#             send_message(response[i])
#
#         # pool.map(send_message, response)
#
#             # for i in range(len(response)):
#             #     p = Process(target=send_message, args=(response[i],))
#             #
#             #     p.start()
#             #     p.join()
#
#         # else:
#         #     pass
#
#     else:
#         print 'e'
