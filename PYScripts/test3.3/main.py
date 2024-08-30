def get_mult_digit(number=0):
    str_num = str(number)
    first = int(str_num[0])
    if first == 0:
        first = 1
    if len(str_num) == 1:
        return first
    else:
        return first * get_mult_digit(int(str_num[1:]))

print(get_mult_digit(40203))