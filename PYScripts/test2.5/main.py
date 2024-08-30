from random import *
def get_matrix(x,y,values=0):
    matrix = []
    rand = False
    if values == 0: rand = True
    for i in range(x):
        addrow = []
        for j in range(y):
            if rand == True:
                addrow.append(randint(1,100))
            else:
                addrow.append(values)
        matrix.append(addrow)
    for i in matrix:
        print(i)

get_matrix(int(input()),int(input()),0)