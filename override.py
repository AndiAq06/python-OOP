class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("show info di class Hero")
        print(f"{self.name} health: {self.health}")


class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    # override
    def showInfo(self):
        print("show info di class Hero_intelligent")
        print(f"{self.name} \n\tTipe: intelligent, \n\thealth: {self.health}")


lina = Hero_intelligent('lina')
lina.showInfo()