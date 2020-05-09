from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import itertools

from explicit import waiter, XPATH
from selenium import webdriver
import time


class InstagramBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()

    def closrBrowser(self):
        self.driver.close()

    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)
        user_name_element=driver.find_element_by_xpath("//input[@name='username']")
        user_name_element.clear()
        user_name_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(10)
        #cancel_notification_button = driver.find_element_by_class_name('HoLwm')
        #cancel_notification_button.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.aOOlW.HoLwm"))).click()
        time.sleep(2)

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(10)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(5)
        #searshing for picture link
        hrefs = driver.find_elements_by_tag_name('a')
        images_links = []
        for item in hrefs:
            href = item.get_attribute('href')
            if "/p/" not in href:
                continue
            #print(href)
            images_links.append(href)

        for images_link in images_links:
            driver.get(images_link)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("coreSpriteHeartOpen").click()
                print("liked")
                time.sleep(10)
            except Exception as e:
                time.sleep(2)
    def follow_users_from_user(self,user):
        driver = self.driver
        driver.get("https://www.instagram.com/"+user+"/?hl=pt-br")
        time.sleep(5)
        waiter.find_element(driver, "//a[@href='/"+user+"/followers/']", by=XPATH).click()
        time.sleep(5)
        #follow = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.BY3EC > button')))
        #follow.click()
        #segui = driver.find_elements_by_class_name('BY3EC')
        #if segui:
        #    segui[0].click()
        for y in range(12):
            #find all li elements in list
            fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
            scroll = 0
            while scroll < 2: # scroll 5 times
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                time.sleep(1)
                scroll += 1

            fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
            print("Dando scroll em {} usuários.".format(len(fList)))

            print("Fim do scroll.")
            for x in range(5):
                try:
                    follow_button = driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
                    follow_button.click()
                    print("[ Usuário seguido! ]")
                    time.sleep(2)
                except:
                    continue
        

        
bot=InstagramBot("ninho.do.template","cruzeiro4")
bot.login()
#bot.follow_users_from_user("templates.ofc")
bot.follow_users_from_user("templatesbrasil")
