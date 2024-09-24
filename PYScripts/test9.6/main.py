def all_variants(str_out):
    numout = 1
    while numout < len(str_out):
        i = 0
        for i in range(len(str_out)):
            if i + numout < len(str_out):
                yield str_out[i:i + numout:]
            else:
                yield str_out[i:len(str_out)]
                break
        numout +=1
    yield str_out


for i in all_variants("lorem"):
   print(i)
