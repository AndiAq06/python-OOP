class Hero:
    # class variabel
    jumlah = 0


    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah += 1
        print(f"Membuat hero dengan nama {self.name}")

hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)