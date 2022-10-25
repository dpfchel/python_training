

import time

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # menu "add new"
        self.open_edit_contacts_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.firstname)  # переиспользуем метод из fixture/group.py
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_telephone)
        self.app.change_field_value("mobile", contact.mobile_telephone)
        self.app.change_field_value("work", contact.work_telephone)
        self.app.change_field_value("fax", contact.fax_telephone)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)
        self.app.change_field_value_select("bday", contact.day_birthday)   # создаем метод для выбора значения в fixture/group.py, где такой же метод ввода значения
        self.app.change_field_value_select("bmonth", contact.month_birthday)
        self.app.change_field_value("byear", contact.year_birthday)
        self.app.change_field_value_select("aday", contact.day_anniversary)
        self.app.change_field_value_select("amonth", contact.month_anniversary)
        self.app.change_field_value("ayear", contact.year_anniversary)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.home_phone2)
        self.app.change_field_value("notes", contact.notes)


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # выбор первого чек-бокса
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[onclick='DeleteSel()'][value='Delete']").click()
        # подтверждаем удаление контакта
        wd.switch_to.alert.accept()
        self.open_home_page()

    def test_modificate_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()


    def open_edit_contacts_page(self):
        wd = self.app.wd
        # menu "add new"
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.get("http://localhost/addressbook/edit.php")


    def open_home_page(self):
        wd = self.app.wd
        # menu "home"
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_css_selector("[value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/index.php")


