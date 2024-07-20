import pytest

def get_data():
    return [
        ("vinay@gmail.com","esaf345"),
        ("kajal@gmail.com","esaferewfsc3434"),
        ("rahul@gmail.com","esaere3434")

    ]
@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    return print(username,"and",password)
