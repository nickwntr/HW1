def calculate_sum(numbers):
    summage = 0
    incorrect_data = 0
    for number in numbers:
        try:
            summage += number
        except TypeError:
            incorrect_data += 1
    print("Результат")
    return (summage, incorrect_data)

def calculate_avg(numbers):
    summage = 0
    nums = 0
    result = 0
    try:
        for number in numbers:
            try:
                summage += number
                nums += 1
            except TypeError:
                print(f'\"{number}\" НЕ являются числом')
    except TypeError:
        print("Элемент не коллекция")
        return None
    try:
        result = summage / nums
    except ZeroDivisionError:
        print("На ноль не делится")
        return 0
    print('Результат:')
    return result


print(calculate_sum([3,6,9,"12"]))
print(calculate_avg([3,6,9,12]))
print(calculate_avg([0,0,0,0]))
print(calculate_avg([]))
print(calculate_avg(2))
print(calculate_avg(["12","12"]))