from money import Money
from portfolio import Portfolio


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


def test_addition():
    five_dollars = Money(5, "USD")
    ten_dollars = Money(10, "USD")
    fifteen_dollars = Money(15, "USD")

    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_dollars)

    assert fifteen_dollars == portfolio.evaluate("USD")

def test_addition_of_dollars_and_euros():
    five_dollars = Money(5, "USD")
    ten_euros = Money(10, "EUR")

    portfolio = Portfolio()
    portfolio.add(five_dollars, ten_euros)

    assert str(Money(17, "USD")) == str(portfolio.evaluate("USD"))

def test_addition_of_dollars_and_wons():
    one_dollar = Money(1, "USD")
    eleven_hundred_won = Money(1100, "KRW")

    portfolio = Portfolio()
    portfolio.add(one_dollar, eleven_hundred_won)

    assert str(Money(2200, "KRW")) == str(portfolio.evaluate("KRW"))
