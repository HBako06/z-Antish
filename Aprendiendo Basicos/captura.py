import pyautogui as robot
import telegram


#button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
#button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
#confirmar = 1465,333
#pyautogui.moveTo(button7location)
#print(pyautogui.position())
#pyautogui.moveTo(button7location)
#pyautogui.moveTo(button7location)
#pyautogui.click()

#punto_colorazul = 1445,429

bot_token = '1893337163:AAHXSEBf-9ibMf67B68lgYv7PNrekXlDNoE'
chat_id = '1850445278'
bot = telegram.Bot(token=bot_token)
#print(bot.get_me())
#numero = int()
bot.send_message(chat_id=chat_id, text = 'hola')

#screenshot = pyautogui.screenshot(region=(50, 50, 400, 300))

screenshot = robot.screenshot()
img = screenshot.getpixel((1445,429))
valor = robot.pixelMatchesColor(1445,429, (7,33,70))
print(valor)
#pyautogui.pixelMatchesColor(500, 400, (225, 228, 229))

#if button7location == confirmar :
#	print("true")
#else:
#	print("False")

'''
print("Verificando...")
			screenshot = pyautogui.screenshot()
			img = screenshot.getpixel((1445,429))
			valor = pyautogui.pixelMatchesColor(1445,429, (7,33,70))
			print(valor)
			if valor == False: # Osea no es azul, sino blanco, encontraod!!!
				registro.close()
				txt= "Encontradoooo"
				print(txt)
				engine.say(txt)
				engine.runAndWait()
				robot.alert("Encontrado!!!!")
				time.sleep(10)
'''

#im = pyautogui.screenshot(region=(0,0, 300, 400))
#im1 = pyautogui.screenshot()
#im2 = pyautogui.screenshot('my_screenshot.png')b