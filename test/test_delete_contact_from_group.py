from fixture.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    # create group.id list
    group = db.get_group_list()
    group_id = []
    for i in group:
        group_id.append(i.id)
    # create contact.id list from contacts not in group
    contact_id = []
    for i in group_id:
        l = db.get_contacts_in_group(Group(id=i))
        for item in l:
            if item.id not in contact_id:
                contact_id.append(item.id)
                if len(contact_id) > 0:
                    app.contact.delete_contact_from_group(item.id, i)