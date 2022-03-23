from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import Login




#with open("login.txt",'r') as lendo:
#  Acess = lendo.read().split('\n')

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

time.sleep(30)

login = driver.find_element_by_name("username")
login.click()

time.sleep(4)

for read in Login.name:
    login.send_keys(read)
    time.sleep(0.3)
    
senha = driver.find_element_by_name("password")


