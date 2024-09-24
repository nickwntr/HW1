my_dict = {
    "alpha":11,
    "beta":22
}
print(my_dict)
print(my_dict["alpha"])
print(my_dict.get("gamma"))
my_dict["charlie"] = 44
my_dict["delta"] = 55
print(my_dict)
print(my_dict.pop("charlie"))
print(my_dict)
my_set = {
    1,
    3,
    5,
    7,
    1,
    3,
    7,
    5,
}
print(my_set)
my_set.add(2)
my_set.add(4)
my_set.remove(1)
print(my_set)