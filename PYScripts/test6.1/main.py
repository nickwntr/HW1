from animal import *
from plant import *

a1 = Mammal("Mammal1")
a2 = Predator("Predator1")
p1 = Flower("Flow1")
p2 = Fruit("Fruit1")
print(a1.name)
print(a2.name)
print(type(a1).__base__.__name__)
a1.eat(p2)
a2.eat(a1)
print(a1.alive)
