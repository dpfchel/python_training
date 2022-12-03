from fixture.contact import Contact

def test_phones_on_home_page(app, db):
    list_contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    list_contacts_home = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(list_contacts_db) == len(list_contacts_home)
    for i in range(len(list_contacts_db)):
        assert list_contacts_db[i] == list_contacts_home[i]
