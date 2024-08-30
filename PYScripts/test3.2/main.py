def print_params(a=1,b='строка',c=True):
    print(a)
    print(b)
    print(c)

print_params()
values_list = ['alpha',42]
print_params(*values_list,"no")
values_dict = {
    'a': 11,
    'b': 7
}
print_params(**values_dict,c="yes")