for i in range(1,1000):
    j = 1
    while i > j:
        if j ** 2 + i ** 2 == (1000 - j - i) ** 2:
            print(i*j*(1000 - j - i))
            break
        else:
            j += 1
