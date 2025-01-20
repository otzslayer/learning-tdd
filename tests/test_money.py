import pytest

from bank import Bank
from money import Money
from portfolio import Portfolio


@pytest.fixture
def bank():
    bank = Bank()
    bank.add_exchange_rate("EUR", "USD", 1.2)
    bank.add_exchange_rate("USD", "KRW", 1100)
    return bank


def test_multiplication():
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


def test_addition(bank):
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")
    fifteen_dollars = Money(15, "USD")

    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_dollars)

    assert fifteen_dollars == portfolio.evaluate(bank, "USD")


def test_addition_of_dollars_and_euros(bank):
    five_dollars = Money(5, "USD")
    ten_euros = Money(10, "EUR")

    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_euros)

    assert str(Money(17, "USD")) == str(portfolio.evaluate(bank, "USD"))


def test_addition_of_dollars_and_wons(bank):
    one_dollar = Money(1, "USD")
    eleven_hundred_won = Money(1100, "KRW")

    portfolio = Portfolio()
    portfolio.add(one_dollar, eleven_hundred_won)

    assert str(Money(2200, "KRW")) == str(portfolio.evaluate(bank, "KRW"))


def test_addition_with_multiple_missing_exchange_rates(bank):
    one_dollar = Money(1, "USD")
    one_euro = Money(1, "EUR")
    one_won = Money(1, "KRW")

    portfolio = Portfolio()
    portfolio.add(one_dollar, one_euro, one_won)

    with pytest.raises(
        Exception,
        match=r"[(USD\->Kalagnid),(EUR\->Kalagnid),(KRW\->Kalagnid)]",
    ):
        portfolio.evaluate(bank, "Kalagnid")


def test_conversion_with_different_rates_between_two_currencies(bank):
    ten_euros = Money(10, "EUR")
    assert bank.convert(ten_euros, "USD") == Money(12, "USD")

    bank.add_exchange_rate("EUR", "USD", 1.3)
    assert bank.convert(ten_euros, "USD") == Money(13, "USD")


def test_conversion_with_missing_exchange_rate(bank):
    ten_euros = Money(10, "EUR")
    with pytest.raises(Exception, match="EUR->Kalagnid"):
        bank.convert(ten_euros, "Kalagnid")
