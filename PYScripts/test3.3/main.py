def print_params(a=1,b='строка',c=True):
    print(a)
    print(b)
    print(c)

print_params()
print()
print_params(b=11)
print()
print_params(c=["data", "array"])
print()
values_list = ['alpha',42]
print_params(*values_list,"no")
print()
values_dict = {
    'a': 11,
    'b': 7
}
print_params(**values_dict,c="yes")
print()
values_list_2 = ["aaaaa",5,777.2]
print_params(*values_list_2)