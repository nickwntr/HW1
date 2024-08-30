numbers = []
for i in range(15):
    numbers.append(i+1)
primes = []
noprimes = []
for i in numbers:
    if (i % 10 == 0) or (i % 5 == 0) or (i % 3 == 0) or (i % 2 == 0):
        noprimes.append(i)
    else:
        primes.append(i)
for i in primes:
    print(i)
for i in noprimes:
    print(i)