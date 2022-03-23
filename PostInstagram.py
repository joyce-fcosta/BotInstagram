from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import Login




class BotInstagram(object):

    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    
    def __init__(self, site):
        self.site = site

    def Acess_Site(self):        
        self.driver.get(self.site)
        time.sleep(30)

    def Click_Item(self,Key_Word):
        login = self.driver.find_element_by_name(Key_Word)
        login.click()
        time.sleep(4)
        return login

        

    def Typing_Site(self, string,Key_Word):        
        for read in string:
            self.Click_Item(Key_Word).send_keys(read)
            time.sleep(0.1)
    
#senha = driver.find_element_by_name("password")



def main():

    Navegation = BotInstagram("https://www.instagram.com/accounts/login/?source=auth_switcher")

    Navegation.Acess_Site()

    Navegation.Click_Item("username")
    Navegation.Typing_Site(Login.name,"username")
    
    Navegation.Click_Item("password")
    Navegation.Typing_Site(Login.password,"password")

main()
