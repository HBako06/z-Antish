from requests import get
import requests, json, base64
from requests.structures import CaseInsensitiveDict

import telebot #pip3 install --upgrade pyTelegramBotAPI


bot = telebot.TeleBot("5621929229:AAFANsJbxJJimxTMzDi0tM8Tk0LlqQ35enU")
chat_id = '886944709' #Mak
grupo_id= '-881503367'

@bot.message_handler(content_types=["chimichanga"])
def bot_mensajes_texto(message):
	bot.send_message(message.grupo_id,"dime papeto lendo que pasó")

@bot.message_handler(commands=["nepe"])
def cmd_responder(message):
	bot.send_message(grupo_id,"a black le gusta")


@bot.message_handler(commands=["dni"])
def cmd_responder(message):

	print("oghola")
	dni = message.text
	dni = dni[-8:]
	#bot.send_message(message.chat.id, dni)
	try:
		url = "https://api.municallao.gob.pe/pide/public/v1/reniec/dni/buscar"


		data = '{"usuario" : "0", "app" : "33", "ip" : "0.0.0.0", "dni" : "%s", "strNumDocumento" : "null"}' % (dni)

		headers = {
		    "Content-Type" : "application/json"
		    }

		response = requests.post(url, data=data, headers=headers)

		data = response.json()

		nombre = data['consultarResponse']['return']['datosPersona']['prenombres']
		apellido_uno = data['consultarResponse']['return']['datosPersona']['apPrimer']
		apellido_dos = data['consultarResponse']['return']['datosPersona']['apSegundo']
		estado = data['consultarResponse']['return']['datosPersona']['estadoCivil']
		restri = data['consultarResponse']['return']['datosPersona']['restriccion']
		direc = data['consultarResponse']['return']['datosPersona']['direccion']
		ubigeo = data['consultarResponse']['return']['datosPersona']['ubigeo']
		photo = data['consultarResponse']['return']['datosPersona']['foto']
		decodeit = open(f'{dni}.jpg', 'wb')
		decodeit.write(base64.b64decode((photo)))
		decodeit.close()

	
		foto = open("./"+dni+".jpg","rb")
		#bot.send_photo(message.chat.id,foto)
		#bot.send_photo(message.chat.id,foto,"Nombre: "+ nombre+"\nPrimer Apellido:"+ apellido_uno+"\nSegundo Apellido: "+ apellido_dos+"\n\nEstado de la Persona: "+ estado+"\nRestricciones: "+ restri+"\n\nDireccion: "+ direc+"\nUbigeo: "+ ubigeo)
		bot.send_photo(grupo_id,foto,"DNI: "+dni +"\nNombre: "+ nombre+"\nPrimer Apellido:"+ apellido_uno+"\nSegundo Apellido: "+ apellido_dos+"\n\nEstado de la Persona: "+ estado+"\nRestricciones: "+ restri+"\n\nDireccion: "+ direc+"\nUbigeo: "+ ubigeo)
	
	except Exception as e:
		bot.send_message(grupo_id,"No se encontró dato alguno")


if __name__=='__main__':
	print("Prendiendo")
	bot.infinity_polling()

