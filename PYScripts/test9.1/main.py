def apply_all_func(int_lins,*functions):
    resultdict = {}
    for exec in functions:
        resultdict[exec.__name__] = exec(int_lins)
    return resultdict

print(apply_all_func([1,2,2,6,8,10,-15],min, max,len,sorted,sum,str))

