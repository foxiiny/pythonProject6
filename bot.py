import telebot
from telebot import types
import pandas as pd
import wikipedia
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode


df = pd.read_csv('kpop_idols.csv')
df['year of birth'] = df['Date of Birth'].str.split('-').map(lambda x: x[0])
df['month of birth'] = df['Date of Birth'].str.split('-').map(lambda x: x[1]).str.lstrip('0')
df['day of birth'] = df['Date of Birth'].str.split('-').map(lambda x: x[2]).str.lstrip('0')
df = df.astype({'year of birth': int})


df_girls = df.loc[df['Gender'] == 'F']
df_boys = df.loc[df['Gender'] == 'M']


oven1 = df[df['month of birth'].isin(['3'])]
oven2 = df[df['month of birth'].isin(['4'])]
oven1 = oven1[oven1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
oven2 = oven2[oven2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])]
oven = pd.concat([oven1, oven2], axis=0, join='outer')

telec1 = df[df['month of birth'].isin(['4'])]
telec2 = df[df['month of birth'].isin(['5'])]
telec1 = telec1[telec1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
telec2 = telec2[telec2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])]
telec = pd.concat([telec1, telec2], axis=0, join='outer')

blizneci1 = df[df['month of birth'].isin(['5'])]
blizneci2 = df[df['month of birth'].isin(['6'])]
blizneci1 = blizneci1[blizneci1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
blizneci2 = blizneci2[blizneci2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                              '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                                              '20', '21'])]
blizneci = pd.concat([blizneci1, blizneci2], axis=0, join='outer')

rak1 = df[df['month of birth'].isin(['6'])]
rak2 = df[df['month of birth'].isin(['7'])]
rak1 = rak1[rak1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
rak2 = rak2[rak2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                               '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'])]
rak = pd.concat([rak1, rak2], axis=0, join='outer')

lev1 = df[df['month of birth'].isin(['7'])]
lev2 = df[df['month of birth'].isin(['8'])]
lev1 = lev1[lev1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
lev2 = lev2[lev2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                       '16', '17', '18', '19', '20', '21'])]
lev = pd.concat([lev1, lev2], axis=0, join='outer')

deva1 = df[df['month of birth'].isin(['8'])]
deva2 = df[df['month of birth'].isin(['9'])]
deva1 = deva1[deva1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
deva2 = deva2[deva2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                                                  '22', '23'])]
deva = pd.concat([deva1, deva2], axis=0, join='outer')

vesy1 = df[df['month of birth'].isin(['9'])]
vesy2 = df[df['month of birth'].isin(['10'])]
vesy1 = vesy1[vesy1['day of birth'].isin(['24', '25', '26', '27', '28', '29', '30', '31'])]
vesy2 = vesy2[vesy2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                                                  '22', '23'])]
vesy = pd.concat([vesy1, vesy2], axis=0, join='outer')

scorp1 = df[df['month of birth'].isin(['10'])]
scorp2 = df[df['month of birth'].isin(['11'])]
scorp1 = scorp1[scorp1['day of birth'].isin(['24', '25', '26', '27', '28', '29', '30', '31'])]
scorp2 = scorp2[scorp2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                                                     '22'])]
scorp = pd.concat([scorp1, scorp2], axis=0, join='outer')

strelec1 = df[df['month of birth'].isin(['11'])]
strelec2 = df[df['month of birth'].isin(['12'])]
strelec1 = strelec1[strelec1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
strelec2 = strelec2[strelec2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                                           '21', '22'])]
strelec = pd.concat([strelec1, strelec2], axis=0, join='outer')

kozerog1 = df[df['month of birth'].isin(['12'])]
kozerog2 = df[df['month of birth'].isin(['1'])]
kozerog1 = kozerog1[kozerog1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
kozerog2 = kozerog2[kozerog2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])]
kozerog = pd.concat([kozerog1, kozerog2], axis=0, join='outer')

vodolei1 = df[df['month of birth'].isin(['1'])]
vodolei2 = df[df['month of birth'].isin(['2'])]
vodolei1 = vodolei1[vodolei1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
vodolei2 = vodolei2[vodolei2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                           '11', '12', '13', '14', '15', '16', '17', '18', '19'])]
vodolei = pd.concat([vodolei1, vodolei2], axis=0, join='outer')

ryby1 = df[df['month of birth'].isin(['2'])]
ryby2 = df[df['month of birth'].isin(['3'])]
ryby1 = ryby1[ryby1['day of birth'].isin(['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
ryby2 = ryby2[ryby2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])]
ryby = pd.concat([ryby1, ryby2], axis=0, join='outer')


bot = telebot.TeleBot('5499483607:AAG0n6VOu0v4d6ysM_nPZMjFuMsbUUMoWjo')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, это бот kpop idols 💜 я помогаю найти айдола с наибольшей совместимостью, '
                                'напиши /reg, чтобы начать или /get_info, чтобы узнать про айдола')


df_final = 0
day = 0
month = 0
year = 0
data = 0
data1 = 0
ddd = pd.to_datetime('2000-1-1')
y = '2000'
idol = df


@bot.message_handler(content_types=['text'])
def start2(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Месяц твоего рождения (одну цифру, если твой месяц <10)?")
        bot.register_next_step_handler(message, get_month)
    elif message.text == '/get_info':
        bot.send_message(message.from_user.id, 'Напиши на русском языке с большой буквы имя айдола, про которого хочешь узнать, '
                                               'если в имени есть буква "ё" тоже обязательно её напиши')
        bot.register_next_step_handler(message, get_info)
    elif message.text == '/getwiki':
        bot.send_message(message.from_user.id, 'Напиши имя айдола, про которого хочешь узнать')
        bot.register_next_step_handler(message, getwiki)
    elif message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, это бот kpop idols 💜 нажми /start, чтобы начать")
    elif message.text == "Hi" or message.text == "hi":
        bot.send_message(message.from_user.id, "Hi, this is kpop idols bot 💜 press /start, to start")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write /start to start and /get_info to know about any idol)")
    elif message.text == '/get_result':
        global idol
        global df
        df.loc[:, 'year_gap'] = abs(df['year of birth'] - year)
        if ddd >= pd.to_datetime(y + '-03-21') and ddd <= pd.to_datetime(y + '-04-20'):
            idol = oven[oven['year of birth'] == oven['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-04-21') and ddd <= pd.to_datetime(y + '-05-21'):
            idol = telec[telec['year of birth'] == telec['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-05-22') and ddd <= pd.to_datetime(y + '-06-21'):
            idol = blizneci[blizneci['year of birth'] == blizneci['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-06-22') and ddd <= pd.to_datetime(y + '-07-22'):
            idol = rak[rak['year of birth'] == rak['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-07-23') and ddd <= pd.to_datetime(y + '-08-21'):
            idol = lev[lev['year of birth'] == lev['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-08-22') and ddd <= pd.to_datetime(y + '-09-23'):
            idol = deva[deva['year of birth'] == deva['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-09-24') and ddd <= pd.to_datetime(y + '-10-23'):
            idol = vesy[vesy['year of birth'] == vesy['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-10-24') and ddd <= pd.to_datetime(y + '-11-22'):
            idol = scorp[scorp['year of birth'] == scorp['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-11-23') and ddd <= pd.to_datetime(y + '-12-22'):
            idol = strelec[strelec['year of birth'] == strelec['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-12-23') and ddd <= pd.to_datetime(y + '-1-20'):
            idol = kozerog[kozerog['year of birth'] == kozerog['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-1-21') and ddd <= pd.to_datetime(y + '-2-19'):
            idol = vodolei[vodolei['year of birth'] == vodolei['year_gap'].min()][0]
        elif ddd >= pd.to_datetime(y + '-2-20') and ddd <= pd.to_datetime(y + '-3-20'):
            idol = ryby[ryby['year of birth'] == ryby['year_gap'].min()]
    elif message.text == '/get_date':
        bot.send_message(message.from_user.id, f"на данный момент дата: {day}-{month}-{year}")
    elif message.text == '/get_idol':
        bot.send_message(message.from_user.id, f"на данный момент айдол: {df}")
    elif message.text == '/get_d':
        bot.send_message(message.from_user.id, f"на данный момент y: {type(y)}")
    else:
        bot.send_message(message.from_user.id, "Sorry, I don't understand 😔 write: /help")




def getwiki(message):
    try:
        wikipedia.set_lang("ru")
        s = message.text
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if len((x.strip())) > 3:
                   wikitext2 = wikitext2+x+'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        bot.send_message(message.from_user.id, wikitext2)
    except Exception as e:
        bot.send_message(message.from_user.id, 'В энциклопедии нет информации об этом')


def get_month(message):
    global month
    try:
        month = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Введи, пожалуйста, цифры. Напиши /reg, чтобы начать заново')
        bot.register_next_step_handler(message, get_month)
    bot.send_message(message.from_user.id, 'День твоего рождения (одну цифру, если день <10)?')
    bot.register_next_step_handler(message, get_day)


def get_day(message):
    global day
    try:
        day = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Введи, пожалуйста, цифры. Напиши /reg, чтобы начать заново')
        bot.register_next_step_handler(message, get_day)
    bot.send_message(message.from_user.id, 'Год твоего рождения?')
    bot.register_next_step_handler(message, get_year)


def get_year(message):
    global year
    global ddd
    global y
    global df
    try:
        year1 = int(list(message.text)[0])
        year2 = int(list(message.text)[1])
        year3 = int(list(message.text)[2])
        year4 = int(list(message.text)[3])
        year = int(message.text)
        ddd = pd.to_datetime(str(year) + '-' + str(month) + '-' + str(day))
        y = str(year)

    except Exception:
        bot.send_message(message.from_user.id, 'Введи, пожалуйста, цифры. Напиши /reg, чтобы начать заново')
        bot.register_next_step_handler(message, get_year)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Твоя дата рождения: ' + str(day) + '-' + str(month) + '-' + str(year) + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(telebot.types.InlineKeyboardButton(text='girl groups', callback_data='g'))
    menu2.add(telebot.types.InlineKeyboardButton(text='boy groups', callback_data='b'))
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Среди каких групп ты хочешь, чтобы мы нашли айдола?', reply_markup=menu2)
    elif call.data == "no":
        global day
        global month
        global year
        day = 0
        month = 0
        year = 0
        bot.send_message(call.message.chat.id, 'Напиши /reg')
    elif call.data == 'g':
        global df
        global df_girls
        df = df_girls
        bot.send_message(call.message.chat.id, 'Скоро мы найдем подходящего айдола 🧙 '
                                               'для того чтобы узнать результат нажми /get_result ✨')
    elif call.data == 'b':
        global df_boys
        df = df_boys
        bot.send_message(call.message.chat.id, 'Скоро мы найдем подходящего айдола 🧙 '
                                               'для того чтобы узнать результат нажми /get_result ✨')


df['year_gap'] = abs(df['year of birth'] - year)


oven1 = df[df['month of birth'].isin(['3'])]
oven2 = df[df['month of birth'].isin(['4'])]
oven1 = oven1[oven1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
oven2 = oven2[oven2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20'])]
oven = pd.concat([oven1, oven2], axis=0, join='outer')


telec1 = df[df['month of birth'].isin(['4'])]
telec2 = df[df['month of birth'].isin(['5'])]
telec1 = telec1[telec1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
telec2 = telec2[telec2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21'])]
telec = pd.concat([telec1, telec2], axis=0, join='outer')

blizneci1 = df[df['month of birth'].isin(['5'])]
blizneci2 = df[df['month of birth'].isin(['6'])]
blizneci1 = blizneci1[blizneci1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
blizneci2 = blizneci2[blizneci2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21'])]
blizneci = pd.concat([blizneci1, blizneci2], axis=0, join='outer')


rak1 = df[df['month of birth'].isin(['6'])]
rak2 = df[df['month of birth'].isin(['7'])]
rak1 = rak1[rak1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
rak2 = rak2[rak2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22'])]
rak = pd.concat([rak1, rak2], axis=0, join='outer')


lev1 = df[df['month of birth'].isin(['7'])]
lev2 = df[df['month of birth'].isin(['8'])]
lev1 = lev1[lev1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
lev2 = lev2[lev2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                       '16', '17', '18', '19','20', '21'])]
lev = pd.concat([lev1, lev2], axis=0, join='outer')


deva1 = df[df['month of birth'].isin(['8'])]
deva2 = df[df['month of birth'].isin(['9'])]
deva1 = deva1[deva1['day of birth'].isin(['22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
deva2 = deva2[deva2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22','23'])]
deva = pd.concat([deva1, deva2], axis=0, join='outer')


vesy1 = df[df['month of birth'].isin(['9'])]
vesy2 = df[df['month of birth'].isin(['10'])]
vesy1 = vesy1[vesy1['day of birth'].isin(['24', '25', '26', '27', '28', '29', '30', '31'])]
vesy2 = vesy2[vesy2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22','23'])]
vesy = pd.concat([vesy1, vesy2], axis=0, join='outer')


scorp1 = df[df['month of birth'].isin(['10'])]
scorp2 = df[df['month of birth'].isin(['11'])]
scorp1 = scorp1[scorp1['day of birth'].isin(['24', '25', '26', '27', '28', '29', '30', '31'])]
scorp2 = scorp2[scorp2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22'])]
scorp = pd.concat([scorp1, scorp2], axis=0, join='outer')


strelec1 = df[df['month of birth'].isin(['11'])]
strelec2 = df[df['month of birth'].isin(['12'])]
strelec1 = strelec1[strelec1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
strelec2 = strelec2[strelec2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19','20', '21', '22'])]
strelec = pd.concat([strelec1, strelec2], axis=0, join='outer')


kozerog1 = df[df['month of birth'].isin(['12'])]
kozerog2 = df[df['month of birth'].isin(['1'])]
kozerog1 = kozerog1[kozerog1['day of birth'].isin(['23', '24', '25', '26', '27', '28', '29', '30', '31'])]
kozerog2 = kozerog2[kozerog2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])]
kozerog = pd.concat([kozerog1, kozerog2], axis=0, join='outer')


vodolei1 = df[df['month of birth'].isin(['1'])]
vodolei2 = df[df['month of birth'].isin(['2'])]
vodolei1 = vodolei1[vodolei1['day of birth'].isin(['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
vodolei2 = vodolei2[vodolei2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19'])]
vodolei = pd.concat([vodolei1, vodolei2], axis=0, join='outer')


ryby1 = df[df['month of birth'].isin(['2'])]
ryby2 = df[df['month of birth'].isin(['3'])]
ryby1 = ryby1[ryby1['day of birth'].isin(['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])]
ryby2 = ryby2[ryby2['day of birth'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])]
ryby = pd.concat([ryby1, ryby2], axis=0, join='outer')



if ddd >= pd.to_datetime(y+'-03-21') and ddd <= pd.to_datetime(y+'-04-20'):
    idol = oven[oven['year of birth'] == oven['year_gap'].min()][0]
elif ddd >= pd.to_datetime(y+'-04-21') and ddd <= pd.to_datetime(y+'-05-21'):
    idol = telec[telec['year of birth'] == telec['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-05-22') and ddd <= pd.to_datetime(y+'-06-21'):
    idol = blizneci[blizneci['year of birth'] == blizneci['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-06-22') and ddd <= pd.to_datetime(y+'-07-22'):
    idol = rak[rak['year of birth'] == rak['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-07-23') and ddd <= pd.to_datetime(y+'-08-21'):
    idol = lev[lev['year of birth'] == lev['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-08-22') and ddd <= pd.to_datetime(y+'-09-23'):
    idol = deva[deva['year of birth'] == deva['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-09-24') and ddd <= pd.to_datetime(y+'-10-23'):
    idol = vesy[vesy['year of birth'] == vesy['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-10-24') and ddd <= pd.to_datetime(y+'-11-22'):
    idol = scorp[scorp['year of birth'] == scorp['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-11-23') and ddd <= pd.to_datetime(y+'-12-22'):
    idol = strelec[strelec['year of birth'] == strelec['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-12-23') and ddd <= pd.to_datetime(y+'-1-20'):
    idol = kozerog[kozerog['year of birth'] == kozerog['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-1-21') and ddd <= pd.to_datetime(y+'-2-19'):
    idol = vodolei[vodolei['year of birth'] == vodolei['year_gap'].min()]
elif ddd >= pd.to_datetime(y+'-2-20') and ddd <= pd.to_datetime(y+'-3-20'):
    idol = ryby[ryby['year of birth'] == ryby['year_gap'].min()]


def get_info(message):
    t = message.text.strip()
    r = requests.get('https://kpop.fandom.com/ru/wiki/' + t)
    soup = BeautifulSoup(r.text, features="html.parser")
    q = soup('h3', class_="pi-data-label pi-secondary-font")
    for i in range(len(q)):
        q[i] = q[i].text.strip()
    a = soup('div', class_="pi-data-value pi-font")
    for i in range(len(a)):
        a[i] = a[i].text.strip()
    d = {'характеристика': q, 'значение': a}
    g = pd.DataFrame(d)
    g.set_index('характеристика', inplace=True)
    if len(g) !=0:
        bot.send_message(message.from_user.id, f"{g['значение']}")
    else:
        bot.send_message(message.from_user.id, 'Пожалуйста, вводите имя с большой буквы.'
                                               ' Если в имени есть буква "ё", обязательно пишите её, а не "е". '
                                               ' Если это не помогает, попробуйте ввести имя в формате: Имя_(Название группы),'
                                               ' например: Хёнджин_(Stray Kids) или Субин_(TXT). Чтобы попробовать еще раз напиши /get_info 💗')


bot.polling(none_stop=True, interval=0)
