class Money:

    _exchange_rate = {
        "EUR": 0.86,
        "BYN": 2.51,
        "JPY": 111.08,
        "USD": 1
    }

    def __init__(self, value, currency="USD"):
        self.value = float(value)
        self.currency = currency

    def __to_default_currency(self):
        return self.value / self._exchange_rate[self.currency]

    def __convert_to(self, currency):
        return self.__to_default_currency() * self._exchange_rate[currency]

    def check(self):
        print(f"{self.value} {self.currency} = {self.__to_default_currency()} USD")
        print(f"{self.value} {self.currency} = {self.__convert_to('EUR')} EUR")

    def __eq__(self, other):
        return self.__to_default_currency() == other.__to_default_currency()

    def __le__(self, other):
        return self.__to_default_currency() <= other.__to_default_currency()

    def __ge__(self, other):
        return self.__to_default_currency() >= other.__to_default_currency()

    def __lt__(self, other):
        return self.__to_default_currency() < other.__to_default_currency()

    def __gt__(self, other):
        return self.__to_default_currency() > other.__to_default_currency()

    def __ne__(self, other):
        return self.__to_default_currency() != other.__to_default_currency()

    def __truediv__(self, other):
        return Money(self.value / other, self.currency)

    def __rtruediv__(self, other):
        return Money(self.value / other, self.currency)

    def __mul__(self, other):
        return Money(self.value * other, self.currency)

    def __rmul__(self, other):
        return Money(self.value * other, self.currency)

    def __add__(self, other):
        return Money(self.value + other.__convert_to(self.currency), self.currency)

    def __radd__(self, other):
        if other == 0:
            return Money(self.value + other, self.currency)
        return Money(self.value + other.__convert_to(self.currency), self.currency)

    def __sub__(self, other):
        return Money(self.value - other.__convert_to(self.currency), self.currency)

    def __rsub__(self, other):
        return Money(self.value - other.__convert_to(self.currency), self.currency)

    def __str__(self):
        return f"{self.value} {self.currency}"


if __name__ == "__main__":
    x = Money(5.02, "BYN")
    y = Money(3)
    z = Money(1.72, "EUR")
    print(y + 3 * x + z * 2)

    lst = [Money(10, "BYN"), Money(5), Money(12000, "JPY")]
    s = sum(lst)
    print(s)
