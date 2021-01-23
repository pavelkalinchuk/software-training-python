import pytest
import json
import jsonpickle
import os.path
import importlib
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
    parser.addoption("--target", action="store", default="target.json")


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
