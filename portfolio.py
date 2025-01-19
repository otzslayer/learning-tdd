import functools
import operator

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except KeyError as e:
                failures.append(e)

        if len(failures) == 0:
            return Money(total, currency)

        failure_message = ",".join(f"{e.args[0]}" for e in failures)
        print(failure_message)
        raise Exception(f"Missing exchange rate(s):[{failure_message}]")
