import math
import pytest

# first testcase
@pytest.mark.skip
def test_floor():
    num = 7
    assert num==math.floor(6.34532)

# second testcase
def test_equal():
    assert 50==49

# third testcase
@pytest.mark.xfail
def test_difference():
    assert  99-43==57

# Fourth testcase
def test_square_root():
    val=8
    assert val==math.sqrt(81)