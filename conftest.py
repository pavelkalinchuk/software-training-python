import importlib
import json
import os.path

import jsonpickle
import pytest

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, base_url=web_config["baseURL"])
    fixture.session.ensure_login(username=web_config["login"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config['host'], database=db_config['database'], user=db_config['user'],
                          password=db_config['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(end)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture_ in metafunc.fixturenames:
        if fixture_.startswith("data_"):  # брать тестовые данные из data/groups.py (статические данные)
            testdata = load_from_module(fixture_[5:])
            metafunc.parametrize(fixture_, testdata, ids=[str(x) for x in testdata])
        elif fixture_.startswith("json_"):  # брать тестовые данные из data/groups.json (файл создается генератором)
            testdata = load_from_json(fixture_[5:])
            metafunc.parametrize(fixture_, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
