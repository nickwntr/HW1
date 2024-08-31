from random import *
def get_matrix(x,y,values):
    matrix = []
    rand = False
    if x > 0 and y > 0:
        if len(values) == 0: rand = True
        for i in range(x):
            addrow = []
            for j in range(y):
                if rand == True:
                    addrow.append(randint(1, 100))
                else:
                    addrow.append(values[randint(0, len(values) - 1)])
            matrix.append(addrow)
        for i in matrix:
            print(i)
    else:print(matrix)

print("Ведите длину, ширину массива, и его данные. Набор данных окончить END")
x = int(input())
y = int(input())
values = []
minusoneterm = True
while minusoneterm:
    inp = input()
    if inp.lower() == "END".lower():
        minusoneterm = False
        break
    else:
        values.append(inp)

get_matrix(x, y, values)
