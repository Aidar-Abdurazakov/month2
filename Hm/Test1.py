class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp):
        super().__init__(name, lvl, hp, 0)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:
    bank_name = "Simba Bank"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return (
            f"Герой: {self.hero.name}, "
            f"Уровень: {self.hero.lvl}, "
            f"Баланс: {self._balance} SOM"
        )

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        raise TypeError("Нельзя складывать счета героев разных классов!")

    def __eq__(self, other):
        return (
            type(self.hero) == type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )


simple_hero = Hero("Алекс", 1, 50)
simple_hero.action()

mage1 = MageHero("Гэндальф", 10, 80, 150)
mage1.action()

mage2 = MageHero("Мерлин", 10, 90, 200)
mage2.action()

warrior = WarriorHero("Конан", 15, 200)
warrior.action()

acc1 = BankAccount(mage1, 1000, "1234")
acc2 = BankAccount(mage2, 500, "1111")
acc3 = BankAccount(warrior, 700, "2222")

print("\nПроверка пароля:")
print(acc1.login("1234"))      
print(acc1.login("0000"))      

print("\nИнформация о счете:")
print(acc1.full_info)

print("\nНазвание банка:")
print(BankAccount.get_bank_name())

print("\nБонус за уровень:")
print(acc1.bonus_for_level())

print("\nМетод __str__:")
print(acc1)

print("\nМетод __add__:")
print(acc1 + acc2)           

print("\nМетод __eq__:")
print(acc1 == acc2)            
print(acc1 == acc3)            
