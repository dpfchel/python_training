from idlelib.browser import file_open

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.file_name = '../driver/login.txt'

    def login(self, username, password):
        wd = self.app.wd
        self.app.contact.open_home_page()
        element = WebDriverWait(wd, 2).until(
            EC.presence_of_element_located((By.NAME, "user"))
        )

        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(password)
        wd.find_element(By.XPATH,"//input[@value='Login']").click()
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(' SessionHelper -- login -- ' + '\n')
            file.write('username - ' + str(username) + " password - " + str(password) + '\n')

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(' SessionHelper -- ensure_logout -- ' + '\n')
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(' SessionHelper -- is_logged_in -- ' + '\n')
            time.sleep(5)
            file.write(str(self.app.wd.find_element(By.XPATH,"xpath=//a[contains(text(),'(admin)')]")) + '\n')
        #wd = self.app.wd
        return len(self.app.wd.find_element(By.XPATH,"xpath=//a[contains(text(),'(admin)')]")) > 0

    def is_logged_in_as(self, username):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(' SessionHelper -- is_logged_in_as -- ' + '\n')
            file.write('username - ' + str(username) + '\n')
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd

        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(' SessionHelper -- get_logged_user -- ' + '\n')
            file.write(str(wd.find_element(By.XPATH,"//div[@id='top']/form/b").text[1:-1]) + '\n')

        return wd.find_element(By.XPATH,"//div[@id='top']/form/b").text[1:-1]

    def ensure_login(self, username, password):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(' SessionHelper -- ensure_login -- ' + '\n')
            file.write('username - ' + str(username) + " password - " + str(password) + '\n')
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                with open(self.file_name, 'a', encoding='utf-8') as file:
                    file.write('Сработало if self.is_logged_in_as(username) ' + '\n')
                return    # выход из метода, если залогинен именно username
            else:
                with open(self.file_name, 'a', encoding='utf-8') as file:
                    file.write('Сработало else для if self.is_logged_in_as(username) ' + '\n')
                self.logout() # если залогин, но не username - выйдем
        self.login(username, password)  # 1) если пользователь не залогинен, то логинемся, 2) или через if-else