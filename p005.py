x = 20
a = 0
n = 0
while a < x-1:
    n += 19*20
    for i in range(1, x+1):
        if n % i != 0:
            a = 0
            break
        else:
            a += 1
print n