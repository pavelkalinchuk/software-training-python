from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")
'''
source = 0 - для получения списка контактов
source = 1 - для получения списка групп
source = 2 - для получения списка контактов в указанной группе
'''
source = "0"

try:
    print("\n" + "*** START ***" + "\n" + "-" * 10)
    l = db.get_contact_list()
    for item in l:
        print(item)
    print("*** Total contacts count: " + str(len(l)) + " ***" + "\n" + "-" * 10)
    l = db.get_group_list()
    for item in l:
        print(item)
    print("*** Total groups count: " + str(len(l)) + " ***" + "\n" + "-" * 10)
    l = db.get_contacts_in_group(Group(id="546"))
    for item in l:
        print(item)
    print("*** Total contacts in group count: " + str(len(l)) + " ***" + "\n" + "-" * 10)
    l = db.get_contacts_not_in_group(Group(id="546"))
    for item in l:
        print(item)
    print("*** Total contacts not in group count: " + str(len(l)) + " ***" + "\n" + "-" * 10)
    print("*** END ***" + "\n")
    a = db.get_group_list()
    print(random.choice(a).id)
finally:
    pass
