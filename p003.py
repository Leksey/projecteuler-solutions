import math

a = 600851475143
primes = [2]
i = 3
for i in range(i, int(math.sqrt(a))+1):
    isPrime = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
j = 1
for p in primes:
    if a % p == 0:
        while a % p == 0:
            a = a / p
        print p
    else:
        j += 1