from house import *


houseBlock1 = House('ЖК Эльбрус', 10)
houseBlock2 = House('ЖК Акация', 20)
print(houseBlock1)
print(houseBlock2)
del houseBlock2
del houseBlock1
print(House.houses_history)