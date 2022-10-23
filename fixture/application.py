# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        self.wd = webdriver.Chrome(executable_path=r'chromedriver.exe')
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_group_page(self):
        wd = self.wd
        # menu "groups"
        wd.get("http://localhost/addressbook/group.php")

    def open_home_page(self):
        wd = self.wd
        # menu "home"
        wd.get("http://localhost/addressbook/index.php")

    def count(self, key):  # key = contact - подсчет контактов, key = group - подсчет групп
        wd = self.wd
        if key == 'group':
            self.open_group_page()
        elif key == 'contact':
            self.open_home_page()
        else:
            print('Неверный параметр! key = contact - подсчет контактов, key = group - подсчет групп')
        return len(wd.find_elements_by_name("selected[]"))


    def destroy(self):
        self.wd.quit()

