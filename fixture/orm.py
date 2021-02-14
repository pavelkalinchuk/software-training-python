# -*- coding: utf-8 -*-
from datetime import datetime

from pony.orm import *

from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        first_name = Optional(str, column="firstname")
        last_name = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host, database, user, password):
        self.db.bind("mysql", host=host, database=database, user=user, password=password)
        self.db.generate_mapping()
        # sql_debug(True)  # вывод тела запроса в консоль

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=contact.id, first_name=contact.first_name, last_name=contact.last_name)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(с for с in ORMFixture.ORMContact))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if orm_group not in c.groups))

    @db_session
    def create_groupid_list(self):
        group_id = []
        for i in self.get_group_list():
            group_id.append(i.id)
        return group_id

    @db_session
    def create_contactid_list_from_contacts_not_in_group(self):
        contact_id = []
        new_contact_id = []
        for i in self.create_groupid_list():
            l = self.get_contacts_not_in_group(Group(id=i))
            for item in l:
                contact_id.append(item.id)
        for i in contact_id:
            if contact_id.count(i) == len(self.get_group_list()) and i not in new_contact_id:
                new_contact_id.append(i)
        return new_contact_id

    @db_session
    def create_contactid_list(self):
        contact_id = []
        for i in self.get_contact_list():
            contact_id.append(i.id)
        return contact_id

    @db_session
    def create_contactid_list_contacts_in_group(self, group):
        contact_id = []
        for i in self.get_contacts_in_group(group):
            contact_id.append(i.id)
        return contact_id
