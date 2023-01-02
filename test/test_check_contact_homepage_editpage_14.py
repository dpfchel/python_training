import re
from random import randrange

def test_phones_on_home_page(app):
    index = randrange(app.count('contact')) #на homepage сходим по индексу, на edit ходим по id
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter( lambda x: x is not None,
                                        #[contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.home_phone2]))))
                                        [contact.home_telephone.strip().replace('/', '').replace('.', ''),
                                         contact.mobile_telephone.strip().replace('/', '').replace('.', ''),
                                         contact.work_telephone.strip().replace('/', '').replace('.', ''),
                                         contact.home_phone2.strip().replace('/', '').replace('.', '')]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             filter ( lambda x: x is not None,
                                      [contact.email, contact.email2, contact.email3])))