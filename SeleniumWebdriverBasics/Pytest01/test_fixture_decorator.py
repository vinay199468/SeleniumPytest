import pytest

@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")
    yield
    print("Closing DB Connection")
@pytest.fixture(scope='function')
def before_function():
    print("Launching browser")
    yield
    print("Closing browser")

@pytest.mark.usefixtures("setup","before_function")
def test_login():
    print("First Testcase")

def test_user_reg():
    print("User Registration Successful")