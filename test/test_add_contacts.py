# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                    nickname="nick", title="title", company="comp", address="address",
                                    home_telephone="home", mobile_telephone="mobile", work_telephone="work",
                                    fax_telephone="fax", email="email1", email2="email2", email3="email3",
                                    homepage="homepage", day_birthday="10", month_birthday="February",
                                    year_birthday="2000", day_anniversary="5", month_anniversary="March",
                                    year_anniversary="2010", address2="address2", home_phone2="home_sec",
                                    notes="notes_sec"))
    app.logout()