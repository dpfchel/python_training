import time
from model.contact import Contact
import re

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
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("[onclick='DeleteSel()'][value='Delete']").click()
        # подтверждаем удаление контакта
        wd.switch_to.alert.accept()
        self.open_home_page()
        self.contact_cache = None

    #def modificate_first_contact(self):
    #    self.modificate_contact_by_index(0)

    def modificate_contact_by_id(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(new_contact_data.id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # переход в модификацию контакта по карандашу с нужным id записи
        str_id = "[href='edit.php?id=%s']" % id  # str_id = "[href='edit.php?id=" + new_contact_data.id + "']"
        wd.find_element_by_css_selector(str_id).click()

    def open_contact_view_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # переход в модификацию контакта по карандашу с нужным id записи
        str_id = "[href='view.php?id=%s']" % id  # str_id = "[href='edit.php?id=" + new_contact_data.id + "']"
        wd.find_element_by_css_selector(str_id).click()

    #def select_first_contact(self):
    #    self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()


    def open_edit_contacts_page(self):
        wd = self.app.wd
        # Если страница не открыта, то откроем страницу
        # menu "add new"
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.get("http://localhost/addressbook/edit.php")


    def open_home_page(self):
        wd = self.app.wd
        # Если страница не открыта, то откроем страницу
        # menu "home"
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_css_selector("[value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    contact_cache = None  # Кэш для get_contact_list, сбрасываем после создания, удаления, модификации контактов

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            i = 2                          # Вариант Алексея - 5- Режем строки на части (00:58)
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                str2 = "//tr[%s]/td[2]" % str(i)  #str2 = "//tr[" + str(i) + "]/td[2]"
                lastname = element.find_element_by_xpath(str2).text
                str3 = "//tr[%s]/td[3]" % str(i)
                firstname = element.find_element_by_xpath(str3).text
                str6 = "//tr[%s]/td[6]" % str(i)
                all_phones = element.find_element_by_xpath(str6).text
                all_phones_list = all_phones.splitlines()
                self.contact_cache.append(Contact(lastname = lastname, firstname = firstname , id = id,
                                                  home_telephone=all_phones_list[0],
                                                  mobile_telephone=all_phones_list[1],
                                                  work_telephone=all_phones_list[2],
                                                  home_phone2=all_phones_list[3]
                                                  ))
                i += 1
        return list(self.contact_cache)   # list - возвращаем копию кэша

    def get_contact_info_from_edit_page(self, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        home_phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone, work_telephone=work_telephone, home_phone2=home_phone2)


    def get_contact_info_from_view_page(self, id):
        wd = self.app.wd
        self.open_contact_view_by_id(id)
        text = wd.find_element_by_id("content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        home_phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, home_phone2=home_phone2)