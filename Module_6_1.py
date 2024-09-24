class Animal:
    def __init__(self,name):
        self.name = name
    alive = True
    fed = False
class Plant:
    def __init__(self,name):
        self.name = name
    edible = False
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True
class Mammal(Animal):
    def eat(self, food):
        if food.edible == False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')
        elif food.edible == True:
            self.fed = True
            print(f'{self.name} сьел {food.name}')
class Predator(Animal):
    def eat(self,food):
        if food.edible == False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')
        elif food.edible == True:
            self.fed = True
            print(f'{self.name} сьел {food.name}')
#_________________________________________________________________________#
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)