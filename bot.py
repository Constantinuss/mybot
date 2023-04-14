import telebot
import datetime
from random import choice

token = '6017304230:AAHPlZfOekCz4VbP-EClLbsEPT24mb6fIk4'

bot = telebot.TeleBot(token)

elp = '''
Список доступных команд:
* напечать все задачи, либо на заданную дату (/show дд.мм.гггг)
* добавить задачу на заданную дату (/add дд.мм.гггг задача)
* /help - Напечатать help
'''

RANDOM_TASKS = ['прыгнуть с парашютом', 'пробежать 50км', 'стать космонавтом', 'посмотреть 4 сезона Рик и Морти', 'сделать доброе дело на ваш выбор', 'заняться рукоделием (что бы это могло означать??? 😳 )']
tasks = {}


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, elp)

@bot.message_handler(commands=['add'])
def add(message):
      b = message.text.split(maxsplit=2) # разбиваю дату задачу
      task = b[2]
      if b[1].lower()  == 'сегодня':
        date = datetime.date.today()
      else:
        b1 = b[1].split('.') # разбиваю дату стр
        dd = int(b1[0])
        mm = int(b1[1])
        yy = int(b1[2])
        date = datetime.date(yy, mm, dd)
      if date in tasks:
        tasks[date].append(task)
      else:
        tasks[date] = []
        tasks[date] = [task]
      bot.send_message(message.chat.id, "Задача добавлена на дату " + date.strftime("%m/%d/%Y"))


@bot.message_handler(commands=['show'])
def show(message):
      b = message.text.split()
      if b[1].lower()  == 'сегодня':
        date = datetime.date.today()
        if date in tasks:
         for task in tasks[date]:
             tasky = [task + ' на сегодня ' + '\n']
             bot.send_message(message.chat.id, tasky)
        else:
         tasky = 'На сегодня ничего не запланировано но можем: ' + choice(RANDOM_TASKS)
         bot.send_message(message.chat.id, tasky)
      else:
        b1 = b[1].split('.') # разбиваю дату стр
        dd = int(b1[0])
        mm = int(b1[1])
        yy = int(b1[2])
        date = datetime.date(yy, mm, dd)
        if date in tasks:
           for task in tasks[date]:
             tasky = [task + ' на дату ' + date.strftime("%m/%d/%Y") + '\n']
             bot.send_message(message.chat.id, tasky)
        else:
          tasky = 'На эту дату ничего не запланировано но можем: ' + choice(RANDOM_TASKS)
          bot.send_message(message.chat.id, tasky)


bot.polling(none_stop=True)
