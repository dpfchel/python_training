# -*- coding: utf-8 -*-
import os.path
import jsonpickle
import getopt
import sys
from random import randrange
from datetime import datetime, timedelta
from fixture.application import Application as appl
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of block x16", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def my_random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    rand_date = start + timedelta(seconds=random_second)
    year = str(rand_date.strftime("%Y"))
    month = str(rand_date.strftime("%B"))
    day = str(int(rand_date.strftime("%d")))
    return [year, month, day]


birthday_rand = my_random_date(datetime.now()-timedelta(days=30*365), datetime.now())
anniversary_rand = my_random_date(datetime.now()-timedelta(days=30*365), datetime.now())
testdata = []
for i in range(n):
    testdata = testdata + [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company,
            address=address, home_telephone=home_telephone, mobile_telephone=mobile_telephone, work_telephone=work_telephone,
            fax_telephone=fax_telephone, email=email, email2=email2, email3=email3, homepage=homepage, day_birthday=day_birthday,
            month_birthday=month_birthday, year_birthday=year_birthday, day_anniversary=day_anniversary, month_anniversary=month_anniversary,
            year_anniversary=year_anniversary, address2=address2, home_phone2=home_phone2, notes=notes)
    for firstname in [(appl.random_string("firstname", 10)).strip()]
    for middlename in [appl.random_string("middlename", 10)]
    for lastname in ["", appl.random_string("lastname", 10)]
    for nickname in [appl.random_string("nickname", 10)]
    for title in [appl.random_string("title", 10)]
    for company in ["", appl.random_string("company", 10)]
    for address in [appl.random_string("address", 10)]
    for home_telephone in [appl.random_string("home_telephone", 10)]
    for mobile_telephone in [appl.random_string("mobile_telephone", 10)]
    for work_telephone in [appl.random_string("work_telephone", 10)]
    for fax_telephone in [appl.random_string("fax_telephone", 10)]
    for email in [appl.random_string("email", 10)]
    for email2 in [appl.random_string("email2", 10)]
    for email3 in ["", appl.random_string("email3", 10)]
    for homepage in [appl.random_string("homepage", 10)]
    for day_birthday in [birthday_rand[2]]
    for month_birthday in [birthday_rand[1]]
    for year_birthday in ["", birthday_rand[0]]
    for day_anniversary in [anniversary_rand[2]]
    for month_anniversary in [anniversary_rand[1]]
    for year_anniversary in [anniversary_rand[0]]
    for address2 in [appl.random_string("address2", 10)]
    for home_phone2 in [appl.random_string("home_phone2", 10)]
    for notes in [appl.random_string("notes", 10)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as ff:
    jsonpickle.set_encoder_options("json", indent=2)
    ff.write(jsonpickle.encode(testdata))
    #

