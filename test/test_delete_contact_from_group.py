from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_for_add_contact_in_group"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(Contact(
            first_name="Test",
            last_name="add contact in group",
            email="add_in_group@mail.com"))
    if len(db.get_contact_list()) == len(db.create_contactid_list_from_contacts_not_in_group()):
        group_id = db.create_groupid_list()[0]
        contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
        app.contact.add_contact_in_group(contact_id, group_id)
        assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))
    for i in db.create_groupid_list():
        if len(db.create_contactid_list_contacts_in_group(Group(id=i))) > 0:
            contact_id = db.create_contactid_list_contacts_in_group(Group(id=i))[0]
            app.contact.delete_contact_from_group(contact_id, i)
            assert contact_id in db.create_contactid_list_from_contacts_not_in_group()
            assert contact_id not in db.create_contactid_list_contacts_in_group(Group(id=i))
