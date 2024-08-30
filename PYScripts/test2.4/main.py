numbers = []
for i in range(15):
    numbers.append(i+1)
primes = []
noprimes = []
for i in numbers:
    if ((i % 10 == 0) and (i / 10 > 1)) or ((i % 5 == 0) and (i / 5 > 1)) or ((i % 3 == 0) and (i / 3 > 1)) or ((i % 2 == 0) and (i / 2 > 1)):
        noprimes.append(i)
    else:
        primes.append(i)
print("Primes: ")
print(primes)
print("Not Primes: ")
print(noprimes)
