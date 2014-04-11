a = 10001
primes = [2]
i = 2
while len(primes) < a:
    i += 1
    isPrime = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
print primes[-1]