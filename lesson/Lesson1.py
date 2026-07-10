class Hero:
    def __init__(self, name, hp, lvl):
        self.hero_name = name
        self.hero_hp = hp
        self.hero_lvl = lvl

Kirito = Hero("Kirito", 1000, 100)
Asuna = Hero("Asuna", 1200, 110)

print(Kirito.hero_lvl)
print(Asuna.hero_lvl)       