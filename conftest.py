import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser, base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser, base_url)
    fixture.session.ensure_login(login, password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(end)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
    parser.addoption("--login", action="store", default="")
    parser.addoption("--password", action="store", default="")
