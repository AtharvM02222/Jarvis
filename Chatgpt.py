from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
ScriptDir = pathlib.Path().absolute()

url = "https://flowgpt.com/"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url=url)
sleep(500)

def Popupremover():
    Xpath = '/html/body/div[3]/div[3]/div/section/button'
    driver.find_element(by=By.XPATH,value=Xpath).click()

Popupremover()
sleep(5000)