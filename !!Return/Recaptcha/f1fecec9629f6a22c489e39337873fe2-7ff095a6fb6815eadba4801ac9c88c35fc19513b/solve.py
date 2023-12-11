import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from capmonster_python import RecaptchaV2Task

API_KEY="9012ea7986eca3ad407310763d5284bb"
WEBSITE_KEY="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
WEBSITE_URL="https://google.com/recaptcha/api2/demo"
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"

# Asegúrate de que la ruta sea la correcta para tu sistema
chromedriver_path = r"C:\WebDriver\chromedriver.exe"  # Cambia esto por tu ruta a ChromeDriver
options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Especifica la ruta al ChromeDriver aquí
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

print("Browser is initialized!")
browser.get(WEBSITE_URL)
print("Browser page is switched to captcha page!")
capmonster = RecaptchaV2Task(API_KEY)
print("ReCaptchaV2 solver initialized!")
print(" -  - - - - - - ")
print(" -  - - - - - - ")

try:
	task_id = capmonster.create_task(WEBSITE_URL, WEBSITE_KEY, no_cache=True)
	print("ReCaptchaV2 solving is begin!")
	result = capmonster.join_task_result(task_id).get("gRecaptchaResponse")
	print("ReCaptchaV2 is solved!")
	browser.execute_script("document.getElementsByClassName(`g-recaptcha-response`)[0].innerHTML = " f"'{result}';")
	print("Result injected to page!")
	browser.find_element(By.ID, "recaptcha-demo-submit").click()
	print("Page submitted!")
	sleep(10)
except Exception as e:
	print(f'error {e}')


