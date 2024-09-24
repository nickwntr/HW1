class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        if step == 0 :
            raise StepValueError
        else:self.step = step
        self.pointer = start
        if step > 0:
            if stop < start:
                raise ValueError("Бесконечная итерация")
        if step < 0:
            if stop > start:
                raise ValueError("Бесконечная итерация")
        self.start -= self.step

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (((self.pointer + self.step > self.stop) and (self.step > 0)) or
                ((self.pointer + self.step < self.stop) and (self.step < 0))):
            raise StopIteration()
        else:
           self.pointer += self.step
           return self.pointer

try:
    for i in Iterator(00,-10, -2):
        print(i)
except ValueError:
    print("Ошибка")
try:
    for i in Iterator(00, 10, -2):
        print(i)
except ValueError:
    print("Ошибка")
try:
    for i in Iterator(10, 0):
        print(i)
except ValueError:
    print("Ошибка")
try:
    for i in Iterator(11, 111, 11):
        print(i)
except ValueError:
    print("Ошибка")




