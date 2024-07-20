import pytest


@pytest.mark.parametrize("num,result", [(1, 11), (2, 22), (3, 13)])
def test_calculation(num, result):
    # result1 = 11 * num
    # print(result1)
    # assert result1 == result
    assert 11*num==result
