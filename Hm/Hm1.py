class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


hero1 = Hero("Артур", 5, 100, 20)
hero2 = Hero("Ланселот", 3, 80, 15)
hero1.greet()
hero1.attack()
hero1.rest()
print("Воин аттакует мечом")

print("После действий:")
print(f"Здоровье: {hero1.health}")
print(f"Сила: {hero1.strength}")

print("-" * 30)
hero2.greet()
hero2.attack()
hero2.rest()

print("После действий:")
print(f"Здоровье: {hero2.health}")
print(f"Сила: {hero2.strength}")