import pytest

def setup_module(module):
    return print("Creating DB Connection")

def teardown_module(module):
    return print("Closing DB connection")

def setup_function(function):
    print("Launching browser")

def teardown_function(function):
    return print("Quitting Browser")

def test_login():
    print("First Testcase")

def test_user_reg():
    print("User Registration Successful")
