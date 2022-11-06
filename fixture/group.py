
#from selenium.webdriver.support.ui import Select
from model.group import Group

class GroupHelper:

    group_cache = None    # Кэш для get_group_list, сбрасываем после создания, удаления, модификации групп

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.group_cache = None # сбрасываем кэш

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None  # сбрасываем кэш

    def modificate_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None  # сбрасываем кэш

    def select_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()


    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value") #без wd ищет внутри element
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache) # list - возвращаем копию кэша





