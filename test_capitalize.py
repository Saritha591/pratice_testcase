import pytest

def test_capital(x):
    return x.capitalize()

def test_capital_case():
    assert test_capital('semaphore') == 'Semaphore'



    