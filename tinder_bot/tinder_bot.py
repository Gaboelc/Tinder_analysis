from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class TinderBot():
    
    def __init__(self, username, password):
        """The bot takes care of logging in and swiping on tinder automatically

        Args:
            username (String): The username used to log in with facebook
            password (String): The password used to log in with facebook
        """
        self.username = username
        self.password = password
        self.webdriver_path = 'webdriver\chromedriver.exe'
        self.drvr = webdriver.Chrome(self.webdriver_path)
        sleep(1)
        
    def login(self):
        """The function automatically accesses and logs into tinder through facebook

        Returns:
            Print: Print that the login was successful
        """
        
        try:
            self.drvr.get('https://tinder.com/')
            sleep(3)

            lg_btn = self.drvr.find_element_by_xpath('//*[@id="c849239686"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
            lg_btn.click()
            sleep(2)

            fb_btn = self.drvr.find_element_by_xpath('//*[@id="c-879141390"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
            sleep(2)

            base_window = self.drvr.window_handles[0]
            sleep(2)
            popup = self.drvr.switch_to.window(self.drvr.window_handles[1])

            email_in = self.drvr.find_element_by_xpath('//*[@id="email"]')
            email_in.send_keys(self.username)
            sleep(1)
            password = self.drvr.find_element_by_xpath('//*[@id="pass"]')
            password.send_keys(self.password)

            login = self.drvr.find_element_by_xpath('//*[@id="loginbutton"]')
            login.click()
            sleep(8)

            self.drvr.switch_to.window(base_window)
            location_permission = self.drvr.find_element_by_xpath('//*[@id="c-879141390"]/div/div/div/div/div[3]/button[1]')
            location_permission.click()
            sleep(2)

            cookie_popup = self.drvr.find_element_by_xpath('//*[@id="c849239686"]/div/div[2]/div/div/div[1]/div[1]/button')
            cookie_popup.click()
            sleep(2)

            notifications_permission = self.drvr.find_element_by_xpath('//*[@id="c-879141390"]/div/div/div/div/div[3]/button[1]')
            notifications_permission.click()
            sleep(2)

            return print('login succesful!! :D')
        except:
            return print('Login failed!! >:(')
        
        
bot = TinderBot('email', 'password')

bot.login()