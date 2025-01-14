import pytest

from money import Dollar, Money
from portfolio import Portfolio


def test_multiplication():
    fiver = Dollar(5)
    tenner = fiver.times(2)

    assert tenner.amount == 10


def test_multiplication_in_dollars():
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")

    assert ten_dollars == five_dollars.times(2)


def test_multiplication_in_euros():
    ten_euros = Money(10, "EUR")
    twenty_euros = ten_euros.times(2)

    assert 20 == twenty_euros.amount
    assert "EUR" == twenty_euros.currency


def test_division():
    original_money = Money(4002, "KRW")
    actual_money_after_division = original_money.divide(4)
    expected_money_after_division = Money(1000.5, "KRW")

    assert (
        expected_money_after_division.amount
        == actual_money_after_division.amount
    )

    assert (
        expected_money_after_division.currency
        == actual_money_after_division.currency
    )


def test_addition():
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")
    fifteen_dollars = Money(15, "USD")

    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_dollars)

    assert fifteen_dollars == portfolio.evaluate("USD")
