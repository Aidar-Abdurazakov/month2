import random
from colorama import Fore, Style


class Hero:
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.hp += 1


class Warrior(Hero):
    def __init__(self, name, lvl, hp, strength, stamina):
        super().__init__(name, lvl, hp, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, lvl, hp, strength, mana):
        super().__init__(name, lvl, hp, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, lvl, hp, strength, stealth):
        super().__init__(name, lvl, hp, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


warrior = Warrior("Воин", 10, 1000, 275, 300)
mage = Mage("Маг", 8, 950, 350, 200)
assassin = Assassin("Ассасин", 12, 1200, 300, 50)

warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

assassin.greet()
assassin.attack()
assassin.rest()

print(Fore.BLUE + "\n=== Мини-игра ===" + Style.RESET_ALL)

choice = input(Fore.GREEN + "Выберите героя (Warrior, Mage, Assassin): ")

heroes = {
    "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin
}

if choice not in heroes:
    print(Fore.RED + "Неверный выбор героя!")
else:
    player = heroes[choice]

    enemy = random.choice(list(heroes.values()))

    print(Fore.MAGENTA + f"\nВы выбрали: {player.name}")
    print(Fore.YELLOW + f"Противник: {enemy.name}")

    if player == enemy:
        print(Fore.BLACK + "Ничья!")

    elif isinstance(player, Warrior) and isinstance(enemy, Assassin):
        print(Fore.GREEN + "Warrior победил!")

    elif isinstance(player, Assassin) and isinstance(enemy, Mage):
        print(Fore.GREEN + "Assassin победил!")

    elif isinstance(player, Mage) and isinstance(enemy, Warrior):
        print(Fore.GREEN + "Mage победил!")

    else:
        print(Fore.GREEN + f"{enemy.name} победил!")