def is_Prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            if (((result % 10 == 0) and (result / 10 > 1))
                    or ((result % 5 == 0) and (result / 5 > 1))
                    or ((result % 3 == 0) and (result / 3 > 1))
                    or ((result % 2 == 0) and (result / 2 > 1))):
                print("Число Составное")
            else:
                print("Число Простое")
        return result
    return wrapper


@is_Prime
def add_three(first,second,third):
    return first + second + third

print(add_three(1,1,1))
print(add_three(1,2,3))
print(add_three(2,8,0))
print(add_three(4,0,4))
