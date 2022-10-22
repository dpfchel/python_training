# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modificate_contact(app):
    app.contact.test_modificate_contact(Contact(firstname="modificate_firstname", middlename="modificate_middlename1", lastname="modificate_lastname",
                                        nickname="modificate_nick", title="modificate_title", company="modificate_comp", address="modificate_address",
                                        home_telephone="999999999", mobile_telephone="8888", work_telephone="7777",
                                        fax_telephone="66666", email="modificate@mod", email2="modificate@2", email3="modificate@3",
                                        homepage="modificate_homepage", day_birthday="2", month_birthday="March",
                                        year_birthday="1000", day_anniversary="10", month_anniversary="February",
                                        year_anniversary="1010", address2="modificate_", home_phone2="11111111",
                                        notes="modificate_notes_sec"))
