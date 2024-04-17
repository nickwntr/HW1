immutable_var = ("Lorem","ipsum")
mutable_var = ["Lorem","ipsum"]
print("immutable")
print(immutable_var)
print("mutable")
print(mutable_var)
#immutable_var[0] = "sir"
mutable_var.append("sir")
print(*immutable_var)
print(*mutable_var)