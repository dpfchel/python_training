# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                    nickname="nick", title="title", company="comp", address="address",
                                    home_telephone="home", mobile_telephone="mobile", work_telephone="work",
                                    fax_telephone="fax", email="email1", email2="email2", email3="email3",
                                    homepage="homepage", day_birthday="10", month_birthday="February",
                                    year_birthday="2000", day_anniversary="5", month_anniversary="March",
                                    year_anniversary="2010", address2="address2", home_phone2="home_sec",
                                    notes="notes_sec")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_contact_2(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname2")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_contact_only_notes(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(notes="notes_sec_343434")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert (len(old_contacts) + 1) == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)