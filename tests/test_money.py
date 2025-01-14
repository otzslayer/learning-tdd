import pytest


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


def test_multiplication():
    fiver = Dollar(5)
    tenner = fiver.times(2)

    assert tenner.amount == 10
