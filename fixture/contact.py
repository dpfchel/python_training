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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("[name='selected[]'][value='%s']" % id).click()


    def open_edit_contacts_page(self):
        wd = self.app.wd
        # Если страница не открыта, то откроем страницу
        # menu "add new"
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.get(self.app.base_url + "/edit.php")


    def open_home_page(self):
        wd = self.app.wd
        # Если страница не открыта, то откроем страницу
        # menu "home"
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_css_selector("[value='Send e-Mail']")) > 0):
            wd.get(self.app.base_url + "/index.php")

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
                str4 = "//tr[%s]/td[4]" % str(i)
                address = element.find_element_by_xpath(str4).text
                str5 = "//tr[%s]/td[5]" % str(i)
                all_email_str = element.find_element_by_xpath(str5).text
                str6 = "//tr[%s]/td[6]" % str(i)
                all_phones_str = element.find_element_by_xpath(str6).text
                all_phones = all_phones_str.splitlines()
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_email_from_home_page=all_email_str, all_phones_from_home_page=all_phones_str))
                i += 1
        return list(self.contact_cache)   # list - возвращаем копию кэша



    def get_contact_info_from_edit_page(self, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        #photo
        #delete
        company = wd.find_element_by_name("company").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        fax_telephone = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        day_birthday = wd.find_element_by_name("bday").get_attribute("value")
        month_birthday = wd.find_element_by_name("bmonth").get_attribute("value")
        year_birthday = wd.find_element_by_name("byear").get_attribute("value")
        day_anniversary = wd.find_element_by_name("aday").get_attribute("value")
        month_anniversary = wd.find_element_by_name("amonth").get_attribute("value")
        year_anniversary = wd.find_element_by_name("ayear").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        home_phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        notes = wd.find_element_by_name("notes").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                       company=company, title=title, address=address, home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone, work_telephone=work_telephone, fax_telephone=fax_telephone,
                       email=email, email2=email2, email3=email3, homepage=homepage, day_birthday=day_birthday,
                       month_birthday=month_birthday, year_birthday=year_birthday, day_anniversary=day_anniversary,
                       month_anniversary=month_anniversary, year_anniversary=year_anniversary, address2=address2,
                       home_phone2=home_phone2, notes=notes, id=id)


    def get_contact_info_from_view_page(self, id):
        wd = self.app.wd
        self.open_contact_view_by_id(id)
        text = wd.find_element_by_id("content").text
        home_telephone = self.search_text_phones_on_view_page("H: (.*)", text)
        mobile_telephone = self.search_text_phones_on_view_page("M: (.*)", text)
        work_telephone = self.search_text_phones_on_view_page("W: (.*)", text)
        home_phone2 = self.search_text_phones_on_view_page("P: (.*)", text)
        return Contact(home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, home_phone2=home_phone2)

    # Для обхода ситуации, когда re.search(liked_text_mask, text) is None
    # то у такого объекта нет метода .group(1)
    def search_text_phones_on_view_page(self, liked_text_mask, text):
        if (re.search(liked_text_mask, text) is not None):
            return re.search(liked_text_mask, text).group(1)
        else: return None

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector("select[name='to_group']").click()
        wd.find_element_by_css_selector("[name='to_group'] [value='%s']" % group.id).click()
        wd.find_element_by_css_selector("[value = 'Add to']").click()

    def del_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("[name='group'][onchange='this.parentNode.submit()']").click()
        wd.find_element_by_css_selector("[onchange='this.parentNode.submit()'] [value='%s']" % group.id).click()
        wd.find_element_by_css_selector("[type='checkbox'][value='%s']" % contact.id).click()
        name_css = 'Remove from "%s"' % group.name
        wd.find_element_by_css_selector("[name='remove'][value = '%s']" % name_css).click()
