
import time


from requests import get
import telegram

#import webbrowser

bot_token = '5713869697:AAFaXJywzglUfVERlxLMaQXQx8i5eyEI8xc'
chat_id = '1850445278' #Has
chat_id2 = '886944709' #Mak

bot = telegram.Bot(token=bot_token)

#ip =get("https://api.ipify.org/").text
#print("your ip :", ip)
#bot.send_message(chat_id=chat_id, text = "Iniciado Oh en coords: "+ ip)
bot.send_message(chat_id=chat_id2,text ="hola")


