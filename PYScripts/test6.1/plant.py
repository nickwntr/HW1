class Plant:
    edible = False
    name = None
    def __init__(self, iName):
        self.name = iName

class Flower(Plant):
    def __init__(self, iName):
        self.name = iName
        self.edible = False

class Fruit(Plant):
    def __init__(self, iName):
        self.name = iName
        self.edible = True