class Hero: # template
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "Andi"
hero1.health = 100


hero2.name = "Bagus"
hero2.health = 200

hero3.name = "Ucup"
hero3.health = 1000

print(hero1)
print(hero2.__dict__)
print(hero3.health)