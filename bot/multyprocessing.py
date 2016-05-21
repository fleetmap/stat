# -*- coding: utf-8 -*-
import sys
import time, random, telepot, pprint, codecs, urllib2, json


import pandas as pd
import numpy as np


# connection = psycopg2.connect(host="localhost", port=5432,
#                       database='postgres', user="postgres", password="kizermyframe09")
# cur = connection.cursor()
decoder = codecs.getincrementaldecoder('zlib')('strict')
def handle2(msg):
    pprint(msg)


def getCar(msg):
    show_keyboard = {'keyboard': [['Построить маршрут к машине'], ['Забронировать', 'Назад']]}
    bot.sendMessage(msg['from']['id'], 'Машина выбрана', reply_markup=show_keyboard)

from geopy.distance import vincenty
def get_top_coords(user_lat_lon,data):

    data['Dist']=data.apply(lambda x:vincenty([x.Latitude,x.Longitude],user_lat_lon).meters,axis=1)
    # try:
    data=data[data.Dist<=3000].sort_values('Dist')[['Provider','ExternalName','ModelName','RegistrationNumber', 'GasPercent','Dist','Latitude','Longitude']][:5]
    #car_info="Автомобиль "+data.ModelName+" доступен в "+data.Dist/5000+ " минутах ходьбы./n Уровень топлива: "+data.GasPercent+ "%."
    return data#data[data.Dist<=1200].sort_values('Dist')[['Provider','ExternalName','ModelName','RegistrationNumber', 'GasPercent','Dist','Latitude','Longitude']].to_dict()



def req (msg):


    req = urllib2.Request('http://www.voidspace.org.uk')
    response = urllib2.urlopen(req)
    the_page = response.read()

    return response

#get user id from message

def getCurrentCar(carNumber):
    res = [x for x in xrange(1, carNumber)]
    show_keyboard = {'keyboard': [res]}
    return show_keyboard


def message(msg):
    if(msg['text'].encode('utf-8') == 'FleetMap'):
        show_keyboard = {'keyboard': [['Найти ближашую машину'], ['Прогноз','Назад']]}
        bot.sendMessage(msg['from']['id'], 'This is a custom keyboard', reply_markup=show_keyboard)


def handle_message(msg):

    try:

        array = []
        car_info = get_top_coords([msg['location']['latitude'], msg['location']['longitude']], all_data)
        car_info['Text']=car_info.apply(lambda x:x.ModelName+u" "+str(round(x.Dist/5000,2))+ u" часов. Топливо: "+str(x.GasPercent)+ u"%.",axis=1)
        car_info.reset_index(drop=True,inplace=True)
        stri=""
        if car_info.shape[0]!=0:
            for ix,row in car_info.iterrows():
                stri+=str(ix+1)+". "+(row['Text'])+"\n"
            res = [str(x) for x in xrange(1, 6)]
            show_keyboard = {'keyboard': [res]}
            bot.sendMessage(msg['from']['id'], stri)


        else:
            progn=get_prediction([msg['location']['latitude'], msg['location']['longitude']])
            stri=u"К сожалению, сейчас свободные автомобили отсутствуют.\nВероятность появления автомобиля в этом районе в течение следующего часа: "+str(round(progn,2))
            bot.sendMessage(msg['from']['id'], stri)
            show_keyboard = {'keyboard': [[u"Да",u"Нет"], ['Назад']]}
            bot.sendMessage(msg['from']['id'], u"Сообщить о появлении автомобиля в течение следующего часа?")
        show_keyboard1 = {'keyboard': [res, ['Назад']]}
        tmp_message = ''
        for i in range(len(res)):
            tmp_message = tmp_message + str(i) + '\n'
            show_keyboard1 = {'keyboard': [res, ['Назад']]}
        bot.sendMessage(msg['from']['id'], 'Выберите машину', reply_markup=show_keyboard1)

        print (car_info)

        # car_info_text = car_info[['Dist']].astype(str)+ u" минутах ходьбы.//n Уровень топлива: "




    except:
        pass
    try:
        if(msg['text'].encode('utf-8') == '/start'):
             bot.sendMessage(msg['from']['id'], 'Привет, я телеграм бот введите контрольную фразу с клавиатуры и будет красиво')

        elif(msg['text'] == 'FleetMap'):

            show_keyboard = {'keyboard': [['Найти ближашую машину'], ['Прогноз', 'Назад']]}
            bot.sendMessage(msg['from']['id'], 'Поиск машины',reply_markup=show_keyboard)

        if(msg['text'].encode('utf-8') == 'Найти ближашую машину'):

            bot.sendMessage(msg['from']['id'], 'Введите ваше геоположение')

            # bot.sendMessage(msg['from']['id'],'Капитан, машина найдена')

        if(msg['text'].encode('utf-8') == 'Прогноз'):
            show_keyboard = {'keyboard': [['Понедельник'], ['Вторник'],['Среда'],['Четверг'],['Пятница'],['Суббота'],['Воскресенье']]}
            bot.sendMessage(msg['from']['id'], 'Выберите день на который хотите посмотреть статистику',reply_markup=show_keyboard)



        if( msg['text'].encode('utf-8') == 'Понедельник' or
            msg['text'].encode('utf-8') == 'Вторник' or
            msg['text'].encode('utf-8') == 'Среда' or
            msg['text'].encode('utf-8') == 'Четверг' or
            msg['text'].encode('utf-8') == 'Пятница' or
            msg['text'].encode('utf-8') == 'Суббота' or
            msg['text'].encode('utf-8') == 'Воскресенье'):
            show_keyboard = {'keyboard': [['Утро'],
                                          ['День'],
                                          ['Вечер'],
                                          ['Ночь']]}
            bot.sendMessage(msg['from']['id'], 'Вы выбрали' + " " + msg['text'].encode('utf-8') + ". " + 'Теперь выберите время суток',reply_markup=show_keyboard)

        if(msg['text'].encode('utf-8') == 'Вернуться'):
            show_keyboard = {'keyboard': [['Найти ближашую машину'], ['Прогноз', 'Назад']]}
            bot.sendMessage(msg['from']['id'], 'Поиск машины',reply_markup=show_keyboard)


        if msg['text'].encode('utf-8') == 'Утро':

            show_keyboard = {'keyboard': [['02:00', '03:00', '04:00', '05:00'], ['06:00', '07:00', '08:00', '09:00'],['10:00', '11:00', '12:00', 'Вернуться']]}
            bot.sendMessage(msg['from']['id'], 'Утром много пробок',reply_markup=show_keyboard)


        if msg['text'].encode('utf-8') == 'День':
            show_keyboard = {'keyboard': [['13:00', '14:00', '15:00', '16:00'], ['17:00', '18:00', '19:00', '20:00'],['Вернуться']]}
            bot.sendMessage(msg['from']['id'], 'Днем нужно работать',reply_markup=show_keyboard)


        if msg['text'].encode('utf-8') == 'Вечер':

            show_keyboard = {'keyboard': [['21:00', '22:00', '23:00'],['Вернуться']]}
            bot.sendMessage(msg['from']['id'], 'Вечером много пробок',reply_markup=show_keyboard)

        if msg['text'].encode('utf-8') == 'Ночь':
            show_keyboard = {'keyboard': [['00:00', '01:00', 'Вернуться']]}
            bot.sendMessage(msg['from']['id'], 'Ночь? Тусить едешь?',reply_markup=show_keyboard)

        if  (msg['text'].encode('utf-8') == '00:00' or
            msg['text'].encode('utf-8') == '01:00' or
            msg['text'].encode('utf-8') == '02:00' or
            msg['text'].encode('utf-8') == '03:00' or
            msg['text'].encode('utf-8') == '04:00' or
            msg['text'].encode('utf-8') == '05:00' or
            msg['text'].encode('utf-8') == '06:00' or
            msg['text'].encode('utf-8') == '07:00' or
            msg['text'].encode('utf-8') == '08:00' or
            msg['text'].encode('utf-8') == '09:00' or
            msg['text'].encode('utf-8') == '10:00' or
            msg['text'].encode('utf-8') == '11:00' or
            msg['text'].encode('utf-8') == '12:00' or
            msg['text'].encode('utf-8') == '13:00' or
            msg['text'].encode('utf-8') == '14:00' or
            msg['text'].encode('utf-8') == '15:00' or
            msg['text'].encode('utf-8') == '16:00' or
            msg['text'].encode('utf-8') == '17:00' or
            msg['text'].encode('utf-8') == '18:00' or
            msg['text'].encode('utf-8') == '19:00' or
            msg['text'].encode('utf-8') == '20:00' or
            msg['text'].encode('utf-8') == '21:00' or
            msg['text'].encode('utf-8') == '22:00' or
            msg['text'].encode('utf-8') == '23:00' or
            msg['text'].encode('utf-8') == '24:00'):

                show_keyboard = {'keyboard': [['Посмотреть прогноз'], ['Вернуться']]}
                bot.sendMessage(msg['from']['id'],'"' + msg['text'].encode('utf-8') + '"', reply_markup=show_keyboard)





        if(msg['text'].encode('utf-8') == 'Назад'):
            show_keyboard = {'keyboard': [['Найти ближашую машину'], ['Прогноз','Назад']]}
            bot.sendMessage(msg['from']['id'], 'Вы вернулись назад, выберете требующуюся команду', reply_markup=show_keyboard)

        try:
            if(msg['text'].encode('utf-8') == '1'):
                getCar(msg)
            elif(msg['text'].encode('utf-8') == '2'):
                getCar(msg)
            elif(msg['text'].encode('utf-8') == '3'):
                getCar(msg)
            elif(msg['text'].encode('utf-8') == '4'):
                getCar(msg)
            elif(msg['text'].encode('utf-8') == '5'):
                getCar(msg)

        except:
            pass

        if(msg['text'].encode('utf-8') == 'Забронировать'):
            if random.randint(0, 10) % 2 == 0:
                show_keyboard = {'keyboard': [['Палец вверх', 'Палец вниз'], ['Назад']]}
                bot.sendMessage(msg['from']['id'], 'Спасибо, что выбрали сервис Делимобиль', reply_markup=show_keyboard)
            else:
                show_keyboard = {'keyboard': [['*', '**', '***','****', '*****'], ['Назад']]}
                bot.sendMessage(msg['from']['id'], 'Спасибо, что выбрали сервис Энитайм', reply_markup=show_keyboard)

        if( msg['text'].encode('utf-8') == '*' or
            msg['text'].encode('utf-8') == '**' or
            msg['text'].encode('utf-8') == '***' or
            msg['text'].encode('utf-8') == '****' or
            msg['text'].encode('utf-8') == '*****' or
            msg['text'].encode('utf-8') == 'Палец вверх'):

            show_keyboard = {'keyboard': [['Подписать соглашение'], ['Назад']]}
            bot.sendMessage(msg['from']['id'], 'Вы оценили машину', reply_markup=show_keyboard)

        elif(msg['text'].encode('utf-8') == 'Палец вниз'):
            bot.sendMessage(msg['from']['id'], 'Выберите другой автомобиль')
            show_keyboard = {'keyboard': [['Назад']]}
            bot.sendMessage(msg['from']['id'], 'Не расстраивайтесь=(', reply_markup=show_keyboard)

        if( msg['text'].encode('utf-8') == 'Подписать соглашение'):
            show_keyboard = {'keyboard': [['Начать аренду'], ['Назад']]}
            bot.sendMessage(msg['from']['id'], 'Назад пути нет', reply_markup=show_keyboard)


        if( msg['text'].encode('utf-8') == 'Начать аренду'):
            show_keyboard = {'keyboard': [['Режим ожидания'], ['Завершить аренду']]}
            bot.sendMessage(msg['from']['id'], 'Аренда начата', reply_markup=show_keyboard)

        if( msg['text'].encode('utf-8') == 'Режим ожидания'):
            show_keyboard = {'keyboard': [['Продолжить аренду'], ['Завершить аренду']]}
            bot.sendMessage(msg['from']['id'], 'Вы вошли в режим ожидания', reply_markup=show_keyboard)

        if( msg['text'].encode('utf-8') == 'Завершить аренду'):
            show_keyboard = {'keyboard': [['Найти ближашую машину'], ['Назад']]}
            bot.sendMessage(msg['from']['id'], 'Спасибо за использование нашего сервиса', reply_markup=show_keyboard)

        if( msg['text'].encode('utf-8') == 'Продолжить аренду'):
            show_keyboard = {'keyboard': [['Режим ожидания'], ['Завершить аренду']]}
            bot.sendMessage(msg['from']['id'], 'Аренда продолжена', reply_markup=show_keyboard)



        try:
            print (msg['text'].encode('utf-8'))
        except:
            print (msg)
    except:
        print('Error')

def get_polygons(geojson):
    # функция возвращает многоугольники районов
    polygons = []
    for AO_num in range(len(geojson['features'])):
        AO_name = geojson['features'][AO_num]['properties']['NAME']
        AO_borders = geojson['features'][AO_num]['geometry']['coordinates']
        AO_num_polygons = len(AO_borders)
        # для каждого многоугольника в районе делаем лист ['название района','лист с координатами'],
        # добавляем в общий список
        for plg in range(AO_num_polygons):
            if AO_num_polygons == 1:
                plg_coordinates = [AO_name, AO_borders[plg]]
            else:
                plg_coordinates = [AO_name, AO_borders[plg][0]]
            polygons.append(plg_coordinates)
    return polygons

def get_dot_region(dot, polygons):
    # функция возвращает район для точки
    # dot: [longitude,latitude]
    regions = []
    for reg in polygons:
        if reg[1].contains_point([dot[1],dot[0]]):
            regions.append(reg[0])
            break
    if regions == []:
        regions.append('Другой')
    return regions[0]

def get_prediction(user_lat_lon):
    from datetime import date, datetime, time, timedelta
    dt1=datetime.now()
    dt = datetime.now() + timedelta(minutes=60)
    user_region=get_dot_region(user_lat_lon,MO_polygons)
    return prognoz[(prognoz.MO_Name==user_region)&(((prognoz.Weekday==dt.weekday())
                                         &(prognoz.Hour==dt.hour))|((prognoz.Weekday==dt1.weekday())
                                                                    &(prognoz.Hour==dt1.hour)))].Number.mean()



col_type={'RecordId':int,'ExternalId':str,'ExternalName':str,'Latitude':str,'Longitude':str, 'RegistrationNumber':str, 'Vin':str,
          'ColorName':str,'ModelName':str, 'UpdatedAt':pd.datetime, 'Provider':int, 'IsOk':int, 'Epoch':int,'Source':str, 'GasPercent':str}


all_data=pd.read_csv('last_epoch.csv',sep=';',encoding='cp1251',dtype=col_type)
all_data.RegistrationNumber.fillna('Х725ОА777',inplace=True)
prognoz=pd.read_csv('real_data_result .csv',encoding='cp1251',sep=';')
prognoz.Weekday=prognoz.Weekday.map({u'пн':1,u'вт':2,u'ср':3,u'чт':4,u'пт':5,u'сб':6,u'вс':7})

bot = telepot.Bot('123506925:AAGo1KwBgf7qb24EpyZtxzQdbC-pRtJIfN8')

from urllib2 import urlopen
from matplotlib.path import Path
mos_reg_url_AO = 'http://gis-lab.info/data/mos-adm/ao.geojson'
mos_reg_url_MO = 'http://gis-lab.info/data/mos-adm/mo.geojson'

reader = codecs.getreader("utf-8")

# муниципальные образования
response_MO = urlopen(mos_reg_url_MO)
mos_reg_data_MO = json.load(reader(response_MO))
MO_polygons = get_polygons(mos_reg_data_MO)
MO_polygons = [[i[0],Path(i[1])] for i in MO_polygons]




bot.notifyOnMessage(handle_message)


while 1:
    time.sleep(10)



