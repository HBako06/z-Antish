from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

# Configure browser
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--disable-blink-features=AutomationControlled")

chromedriver = ChromeDriverManager(chrome_type=ChromeType.GOOGLE, 
                                            log_level='0', 
                                            print_first_line=False).install()
driver = webdriver.Chrome(chromedriver, 
                                options=options,
                                service_log_path=None,
                                executable_path="chromedriver.exe")
driver.get("https://enlinea.bancomercio.com/hb/loginhome.jsf")

input ("End?")