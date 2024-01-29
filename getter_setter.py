class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return (f"name {self.name} : \n\thealth: {self.__health}")
    
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = value
    
    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None


sniper = Hero('sniper', 100, 10)

print('merubah info')
print(sniper.info)
print(sniper.__dict__)
sniper.name = "andi"
print(sniper.info)
print(sniper.__dict__)

print('getter and setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print('delete armor')
del sniper.armor
print(sniper.__dict__)