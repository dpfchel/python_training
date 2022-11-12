import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]  #на homepage сходим по индексу, на view, edit ходим по id
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0] #на homepage сходим по индексу, на view, edit ходим по id
    contact_from_view_page = app.contact.get_contact_info_from_view_page(contact_from_home_page.id)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter( lambda x: x is not None,
                                        [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.home_phone2]))))

