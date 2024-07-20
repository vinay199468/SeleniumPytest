import pytest
string_match = "Geeks for Geeks"
# @pytest.mark.xfail
def test_remove_G():
    assert string_match.replace('G','A') == "Aeeks for Aeeks"
    # return print(string_match)
@pytest.mark.skip
def test_remove_e():
    assert string_match.replace("e"," ")=="Gaks for Gaks"