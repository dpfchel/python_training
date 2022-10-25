# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select

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

    """def open_group_page(self):
        wd = self.wd
        # menu "groups"
        wd.get("http://localhost/addressbook/group.php")"""

    """def open_home_page(self):
        wd = self.wd
        # menu "home"
        wd.get("http://localhost/addressbook/index.php")"""

    def count(self, key):  # key = contact - подсчет контактов, key = group - подсчет групп
        wd = self.wd
        if key == 'group':
            self.group.open_groups_page()
        elif key == 'contact':
            self.contact.open_home_page()
        else:
            print('Неверный параметр! key = contact - подсчет контактов, key = group - подсчет групп')
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_select(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)


    def destroy(self):
        self.wd.quit()

