first = ['String',"Student","Computer"]
second = ['Cтрока', "Список", "Компьютер"]

first_result = (abs(len(x[0]) - len(x[1])) if len(x[0]) != len(x[1]) else 0 for x in zip(first,second))
second_result = (abs(len(first[i]) - len(second[i])) if len(first[i]) != len(second[i]) else 0 for i in range(3))

for res in first_result:
    print(res)
print("_---------_")
for res in second_result:
    print(res)
