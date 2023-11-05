from requests import get
import requests, json
from requests.structures import CaseInsensitiveDict

import telebot #pip3 install --upgrade pyTelegramBotAPI


bot = telebot.TeleBot("5621929229:AAFANsJbxJJimxTMzDi0tM8Tk0LlqQ35enU")
#chat_id = '886944709' #Mak
grupo_id= '-1001854996197'


@bot.message_handler(commands=["cod"])
def cmd_responder(message):

	cod = message.text
	cod = cod[-6:]

	url = f"https://upn-api.u-planner.com/api/user-api/getUserList?txt=n00{str(cod)}"
	token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ik4wMDI1NjAwMUB1cG4ucGUiLCJ1c2VySWQiOjM1Nzc1MiwiZW50ZXJwcmlzZUlkIjpudWxsLCJpYXQiOiIyMDIyLTExLTA2VDE3OjMzOjI5LjU4OFoiLCJqdGkiOiJhNzUzMGUyMS04MjE1LTQ4ZjItYjM4Ni0yYTE3N2YyNDUyZTciLCJleHAiOjE2Njc4NDI0MDl9.hfwM8HlzzIfnc6p2Nti5Q_qr2MsnitYo_RbCXjPFgAA"
  	_headers = {'Authorization': token }

	response = requests.get(url, headers=_headers)
	dataJson = response.json()

	if(dataJson['data'] == []):
		print("No existe")
		bot.send_message(grupo_id,"No existe...")
		return

	persona = dataJson['data']
	#print(persona)
	d1 = persona[0]['userId']
	d2 = persona[0]['userName']
	d3 = persona[0]['userCode']
	#print(d2)
	bot.send_message(grupo_id,"userId:    " + str(d1))
	bot.send_message(grupo_id,"userName:  " + str(d2))
	bot.send_message(grupo_id,"userCode:  " + str(d3))
	
	
if __name__=='__main__':
	print("Prendiendo")
	bot.infinity_polling()

