def add_everything(a, b):
    sum = ""
    try:
        sum = a + b
    except:
        sum = f"{a}{b}"
    return sum

print(add_everything(2,"3"))
print(add_everything(2,3))
print(add_everything("2","3"))
print(add_everything("2",3))