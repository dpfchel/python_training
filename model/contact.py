

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_telephone=None, mobile_telephone=None, work_telephone=None, fax_telephone=None,
                 email=None, email2=None, email3=None, homepage=None, day_birthday=None, month_birthday=None,
                 year_birthday=None, day_anniversary=None, month_anniversary=None, year_anniversary=None, address2=None,
                 home_phone2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax_telephone = fax_telephone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.day_birthday = day_birthday
        self.month_birthday = month_birthday
        self.year_birthday = year_birthday
        self.day_anniversary = day_anniversary
        self.month_anniversary = month_anniversary
        self.year_anniversary = year_anniversary
        self.address2 = address2
        self.home_phone2 = home_phone2
        self.notes = notes