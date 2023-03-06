import pytest


@pytest.mark.xfail
def test_upper():
    num = 100
    assert num > 100


@pytest.mark.xfail
def test_upper_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
@pytest.mark.others
def test_lower():
    num = 100
    assert num < 200
