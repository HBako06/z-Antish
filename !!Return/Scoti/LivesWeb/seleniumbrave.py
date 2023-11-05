# Required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Define Brave path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver_path = "chromedriver.exe"


option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito")
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://mi.scotiabank.com.pe/login")
input()