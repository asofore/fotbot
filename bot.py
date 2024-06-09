import requests
from requests import get
from telebot import TeleBot

token='7325290544:AAEGNhJLPtcuXnqzJZxkJ950EjplJnuWsLc'

bot=TeleBot(token)


starts='''
**Hello, I'm a bot.**

**I can give you any image you want.**

**Just tell me what you're looking for.** 
'''





def research(text,chat_id):
	api_key ="AIzaSyBmloDzpd0VB7DwH7UaAXHRx7Qo2Euvw5o"
	sear = "f1af4421d7e134eb1"
	sr = text
	url = "https://www.googleapis.com/customsearch/v1"

	params = {
            'q': sr,
            'key': api_key,
            'cx': sear,
            'searchType': 'image'
            }

	response = requests.get(url, params=params)



	g=response.json()['items']
	jk=[]
	for i in g:
		jk.append(i['link'])
	return jk



@bot.message_handler(commands=['start'])
def st(message):
	bot.send_message(message.chat.id,starts)





@bot.message_handler(func=lambda message : True)
def rger(message):
	ids=message.chat.id
	text= research(message.text,ids)
	for i in text:
		bot.send_photo(ids,i)
	




bot.infinity_polling()


