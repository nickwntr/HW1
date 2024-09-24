ImmutableVar = (1, 2, 8, 7, 33, 756)
print(ImmutableVar)
#ImmutableVar[2] = 10
#^^^^^^^^^^^^^^^^^^^^
#Кортеж не поддерживает переназначение эл-тов
MutableVar = [7,11,77,3346,6875,11]
print(MutableVar)
MutableVar[0]=-1
MutableVar[4] = -7777
print(MutableVar)