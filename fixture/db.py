import pymysql.cursors

from model.group import Group


class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host,
        self.database = database,
        self.user = user,
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id_, name, header, footer) = row
                list_groups.append(Group(id=str(id_), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_groups

    def destroy(self):
        self.connection.close()
