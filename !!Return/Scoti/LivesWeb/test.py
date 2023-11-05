from seleniumbase import Driver
import time

driver = Driver(uc=True)
driver.get("https://enlinea.tarjetaoh.pe/login")
time.sleep(6)
input()
driver.quit()