from fixture.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_for_add_contact_in_group"))
    # create group.id list
    group = db.get_group_list()
    group_id = []
    for i in group:
        group_id.append(i.id)
    # create contact.id list from contacts not in group
    contact_id = []
    for i in group_id:
        l = db.get_contacts_not_in_group(Group(id=i))
        for item in l:
            if item.id not in contact_id:
                contact_id.append(item.id)
    # add contact in group
    app.contact.add_contact_in_group(random.choice(contact_id), random.choice(group_id))

# def test_add_contact_in_group(app):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test_for_add_contact_in_group"))
#     group = random.choice(db.get_group_list())
#     contact = random.choice(db.get_contact_list())
#     app.contact.add_contact_in_group(contact.id, group.id)
#     app.contact.return_home_page()
#     time.sleep(3)
