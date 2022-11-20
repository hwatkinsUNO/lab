import pytest
from account import *

class Test:
    def setup_method(self):
        self.testing = Account('Sample')

    def teardown_method(self):
        del self.testing

    def test_init(self):
        assert self.testing.get_name() == 'Sample'
        assert self.testing.get_balance() == 0

    def test_deposit(self):
        assert self.testing.deposit(-1.25) == False
        assert self.testing.deposit(0) == False
        assert self.testing.deposit(3.50) == True

    def test_withdraw(self):
        self.testing.deposit(5)
        assert self.testing.withdraw(-1.25) == False
        assert self.testing.withdraw(0) == False
        assert self.testing.withdraw(3.50) == True
        assert self.testing.withdraw(2.50) == False










