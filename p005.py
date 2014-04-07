n = 1
a = 0
while a < 19:
    n /= 20
    n += 19
    n *= 20
    for i in range(1, 21):
        if n % i != 0:
            a = 0
            break
        else:
            a += 1
print n