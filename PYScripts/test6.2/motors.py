import random


class Vehicle:
    _COLOR_VARIANTS = ['Yellow', "Black", "White", "Greem", "Olive"]

    def __init__(self, nowner, nmodel, nhp):
        self.owner = nowner
        self._model = nmodel
        self._engine_power = nhp
        self._color = self._COLOR_VARIANTS[random.randrange(0, len(self._COLOR_VARIANTS)-1)]

    def getmodel(self):
        print(f"Модель {self._model}")

    def gethorsepower(self):
        print(f"Мощность {self._engine_power}")

    def getcolor(self):
        print(f"Цвет {self._color}")

    def printinfo(self):
        self.getmodel()
        self.gethorsepower()
        self.getcolor()
        print(f"Владелец: {self.owner}")

    def setcolor(self, ncolor):
        for color in self._COLOR_VARIANTS:
            if color.lower() == ncolor.lower():
                self._color = color
                return
        print("Цвет не найден")


class Sedan(Vehicle):
    _PASSENGERSLIMIT = 5

    def getpasslimit(self):
        print(self._PASSENGERSLIMIT)

    def printinfo(self):
        self.getmodel()
        self.gethorsepower()
        self.getcolor()
        self.getpasslimit()
        print(f"Владелец: {self.owner}")
