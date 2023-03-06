import pytest


@pytest.fixture
def input_value():
    value = 39
    assert value


def test_divisible_by_3(input_value):
    assert input_value % 3 == 1


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
