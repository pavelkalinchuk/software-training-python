import pytest
from fixture.appgroup import Application


@pytest.fixture (scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
