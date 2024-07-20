import pytest

def test_validate_titles():
    expected_title = "Google.com"
    actual_title= "Gmail.com"
    title = "Title name is Google"
    assert expected_title == actual_title, "Title not matched"
    assert "Google" in title
    assert False, "Forcefully failing the test"