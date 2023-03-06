import pytest


@pytest.mark.order(3)
def test_fool():
    assert True


@pytest.mark.order(1)
def test_bar():
    assert True


@pytest.mark.order(4)
def test_success():
    assert True


@pytest.mark.order(2)
def test_food():
    assert True
