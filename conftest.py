import pytest

from test_wallet import Wallet

@pytest.fixture
def my_wallet():
   '''Returns a Wallet instance with a zero balance'''
   assert Wallet()

 
@pytest.fixture
def important_value():
    important = True
    return important

