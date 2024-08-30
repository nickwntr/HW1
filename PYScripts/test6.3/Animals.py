class Horse:
    x_distance = 0
    sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = "I Eat, Sleep, Train, Repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def getpos(self):
        pos = (self.x_distance, self.y_distance)
        print(pos)

    def voice(self):
        print(self.sound)
