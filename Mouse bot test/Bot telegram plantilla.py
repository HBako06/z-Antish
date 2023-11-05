#https://api.telegram.org/bot5436302048:AAET9-hW1YuaAKDBS70Pn5a0IqkKkxUICp0/getUpdates
import telegram
from requests import get

#Telegram:
bot_token = '5436302048:AAET9-hW1YuaAKDBS70Pn5a0IqkKkxUICp0'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)

#bot.send_message(chat_id=chat_id, text = "")

#Ip:
#ip =get("https://api.ipify.org/").text
#print("your ip :", ip)

#ApiSunat Test:
dni=46027897
appiTest =get("https://api.apis.net.pe/v1/dni?numero=",dni).text

print(appiTest)

#bot.send_message(chat_id=chat_id, text = appiTest)

