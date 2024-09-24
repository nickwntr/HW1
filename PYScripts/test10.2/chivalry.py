from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name} атакован ",end="\n")
        enemies = 100
        fighting = True
        i = 0
        while self.power < enemies:
            print(f"{self.name} сражается на протяжении {i} дней. Врагов осталось: {enemies} ", end="\n")
            i += 1
            enemies -= self.power
            sleep(1)
        print(f"{self.name} одолел врагов после {i} дней сражений ",end="\n")


