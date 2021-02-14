from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    if len(db.get_group_list()) == 0 and len(db.get_contact_list()) == 0:
        app.group.create(Group(name="test_for_add_contact_in_group"))
        app.contact.add_new_contact(Contact(
            first_name="Test",
            last_name="add contact in group",
            email="add_in_group@mail.com"))
        group_id = db.create_groupid_list()[0]
        contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
        app.contact.add_contact_in_group(contact_id, group_id)
        assert len(db.get_contacts_in_group(Group(id=group_id))) > 0
        assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))

    if len(db.get_group_list()) == 0 and len(db.get_contact_list()) > 0:
        app.group.create(Group(name="test_for_add_contact_in_group"))
        group_id = db.create_groupid_list()[0]
        contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
        app.contact.add_contact_in_group(contact_id, group_id)
        assert len(db.get_contacts_in_group(Group(id=group_id))) > 0
        assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))

    if len(db.get_group_list()) > 0 and len(db.get_contact_list()) == 0:
        old_contacts = db.get_contact_list()
        app.contact.add_new_contact(Contact(
            first_name="Test",
            last_name="add contact in group",
            email="add_in_group@mail.com"))
        group_id = db.create_groupid_list()[0]
        contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
        app.contact.add_contact_in_group(contact_id, group_id)
        new_contacts = db.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))

    if len(db.get_group_list()) > 0 and len(db.get_contact_list()) > 0:
        if len(db.create_contactid_list_from_contacts_not_in_group()) == 0:
            app.contact.add_new_contact(Contact(
                first_name="Test",
                last_name="add contact in group",
                email="add_in_group@mail.com"))
            group_id = db.create_groupid_list()[0]
            contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
            app.contact.add_contact_in_group(contact_id, group_id)
            assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))
        if len(db.create_contactid_list_from_contacts_not_in_group()) > 0:
            group_id = db.create_groupid_list()[0]
            contact_id = db.create_contactid_list_from_contacts_not_in_group()[0]
            app.contact.add_contact_in_group(contact_id, group_id)
            assert contact_id in db.create_contactid_list_contacts_in_group(Group(id=group_id))


