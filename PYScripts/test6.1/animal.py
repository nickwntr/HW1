from plant import *


class Animal:
    alive = True
    fed = False
    name = None

    def __init__(self, iName):
        self.name = iName


class Mammal(Animal):

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):

    def eat(self, food):
        if type(food).__base__.__name__ == 'Animal':
            print(f"{self.name} съел {food.name}")
            self.fed = True
            food.alive = False
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
