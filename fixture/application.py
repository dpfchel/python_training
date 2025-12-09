# -*- coding: utf-8 -*-
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

from selenium.webdriver.common.by import By

import random
import string


class Application:
    def __init__(self, browser, base_url):
        if browser == 'chrome':
            #chrome_options = webdriver.ChromeOptions()
            #chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            #self.wd = webdriver.Chrome(executable_path=r'/usr/bin/google-chrome-stable')   #chromedriver.exe
            # Автоматически скачивается нужный драйвер
            service = ChromeService('../driver/chromedriver')  # 'c:/python312/chromedriver.exe' укажите путь к вашему chromedriver.exe
            self.wd = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.wd = webdriver.Chrome(service=service)
        elif browser == 'firefox':
            #self.wd = webdriver.Firefox(executable_path=r'geckodriver.exe')
            # Запускаем браузер Firefox с автоматической загрузкой нужного драйвера
            self.wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == 'edge':
            #self.wd = webdriver.Edge(executable_path=r'msedgedriver.exe')
            # Запускаем браузер Edge с автоматической загрузкой нужного драйвера
            self.wd = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError("Unrecognazed browser %s" % browser)
        #self.wd.implicitly_wait(5)
        # Устанавливаем время ожидания (например, 10 секунд)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url=base_url
        #self.wd.get(self.base_url)
        #time.sleep(3)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def count(self, key):  # key = contact - подсчет контактов, key = group - подсчет групп
        wd = self.wd
        if key == 'group':
            self.group.open_groups_page()
        elif key == 'contact':
            self.contact.open_home_page()
        else:
            print('Неверный параметр! key = contact - подсчет контактов, key = group - подсчет групп')
        return len(wd.find_elements(By.NAME, "selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element(By.NAME,  field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_field_value_select(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_number(prefix, maxlen):
        symbols = string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def destroy(self):
        self.wd.quit()

