import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    # base_url = request.config.getoption("--baseURL")
    # login = request.config.getoption("--login")
    # password = request.config.getoption("--password")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, base_url=target["baseURL"])
    fixture.session.ensure_login(username=target["login"], password=target["password"])
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
    # parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
    # parser.addoption("--login", action="store", default="admin")
    # parser.addoption("--password", action="store", default="secret")
    parser.addoption("--target", action="store", default="target.json")
