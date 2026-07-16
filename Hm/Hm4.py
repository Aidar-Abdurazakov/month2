class Money:
    rates = {
        "KGS": 1,
        "USD": 89,
        "EUR": 96,
        "RUB": 1.2
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * Money.rates[self.currency]

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)

        total = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total, "KGS")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)

        total = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total, "KGS")

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"



money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
money3 = Money(50, "USD")

print(money1)        
print(money2)         

print(money1 + money2)   
print(money1 - money2)   
print(money1 + money3)   

print(money1 * 3)      
print(money1 / 2)        