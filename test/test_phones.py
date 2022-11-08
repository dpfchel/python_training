import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    id = contact_from_home_page.id
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(id)
    assert contact_from_home_page.home_telephone == clear(contact_from_edit_page.home_telephone)
    assert contact_from_home_page.work_telephone == clear(contact_from_edit_page.work_telephone)
    assert contact_from_home_page.mobile_telephone == clear(contact_from_edit_page.mobile_telephone)
    assert contact_from_home_page.home_phone2 == clear(contact_from_edit_page.home_phone2)

def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    id = contact_from_home_page.id
    contact_from_view_page = app.contact.get_contact_info_from_view_page(id)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(id)
    assert contact_from_view_page.home_telephone == contact_from_edit_page.home_telephone
    assert contact_from_view_page.work_telephone == contact_from_edit_page.work_telephone
    assert contact_from_view_page.mobile_telephone == contact_from_edit_page.mobile_telephone
    assert contact_from_view_page.home_phone2 == contact_from_edit_page.home_phone2

def clear(s):
    return re.sub("[() -]", "", s)

