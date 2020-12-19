def test_delete_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_all_contacts()
    app.session.logout()