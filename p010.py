a = 2000000
primes = [2]
s = 2
i = 3
for i in range(i, a+1):
    isPrime = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
        s += i
        
print(s)