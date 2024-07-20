import pytest

@pytest.mark.regression
def test_login():
    print("First Testcase")

@pytest.mark.sanity
def test_user_reg():
    print("User Registration Successful")

@pytest.mark.regression
def test_email_compose():
    print("Email compose")

@pytest.mark.skip
def test_skip():
    print("Test Skip")
