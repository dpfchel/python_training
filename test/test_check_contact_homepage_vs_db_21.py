import re
from fixture.contact import Contact

def test_phones_on_home_page(app, db):
    with open('c:/temp/21_list_contacts_home_i.firstname.txt', 'w') as f:
        f.write('')
    with open('c:/temp/21_list_contacts_db_i.firstname.txt', 'w') as f:
        f.write('')

    list_contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    list_contacts_home = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(list_contacts_db) == len(list_contacts_home)
    for i in range(len(list_contacts_db)):
        list_contacts_home_i = list_contacts_home[i]
        list_contacts_db_i = list_contacts_db[i]
        assert list_contacts_home_i.firstname == list_contacts_db_i.firstname
        assert list_contacts_home_i.lastname == list_contacts_db_i.lastname
        assert list_contacts_home_i.address == list_contacts_db_i.address
        assert list_contacts_home_i.all_email_from_home_page == merge_email_like_on_home_page(list_contacts_db_i)
        assert list_contacts_home_i.all_phones_from_home_page == merge_phones_like_on_home_page(list_contacts_db_i)

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