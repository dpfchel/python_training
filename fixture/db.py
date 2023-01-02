import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list
# contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.home_phone2
    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            sql_my = "select " \
                     "id, " \
                     "firstname, " \
                     "lastname, " \
                     "address, " \
                     "email, email2, email3, " \
                     "home, mobile, work, phone2 " \
                     "from addressbook " \
                     "where deprecated='0000-00-00 00:00:00'"
            cursor.execute(sql_my)
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname.strip(), lastname=lastname.strip(),
                                    address=address.strip(), email=email.strip(), email2=email2.strip(),
                                    email3=email3.strip(),
                                    home_telephone=home,
                                    mobile_telephone=mobile,
                                    work_telephone=work,
                                    home_phone2=phone2
                                    #home_telephone=home.strip().replace('/', '').replace('.', ''),  # Решил убирать лишние символы в самом тесте
                                    #mobile_telephone=mobile.strip().replace('/', '').replace('.', ''),  #убираю из телефонов последние пробелы, слеш, точку, для сравнения с выводимым на экран
                                    #work_telephone=work.strip().replace('/', '').replace('.', ''),
                                    #home_phone2=phone2.strip().replace('/', '').replace('.', '')
                                    ))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()


