class House:
    def __init__(self, nName, nfloorNum):
        self.name = nName
        self.floorNum = nfloorNum

    def go_to_floor(self, new_floor):
        if (new_floor < self.floorNum) and (new_floor > 1):
            print(f"Вы на {new_floor}-м этаже")
        else:
            print("Этаж не найден")

    def __len__(self):
        return self.floorNum

    def __str__(self):
        return f"Название: {self.name}. Кол-во этажей: {self.floorNum}"

    def __eq__(self, other):
        return self.floorNum == other.floorNum

    def __lt__(self, other):
        return self.floorNum < other.floorNum

    def __le__(self, other):
        return self.floorNum <= other.floorNum

    def __gt__(self, other):
        return self.floorNum > other.floorNum

    def __ge__(self, other):
        return self.floorNum >= other.floorNum

    def __add__(self, value):
        self.floorNum += value
        return self

    def __radd__(self, value):
        self.floorNum += value
        return self

    def __iadd__(self, value):
        self.floorNum += value
        return self