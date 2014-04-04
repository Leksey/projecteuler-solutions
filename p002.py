f = [0,1]
while f[-1] < 4000000:
    f.append(f[-2]+f[-1])

del f[-1]
result = 0
for i in f:
    if i % 2 ==0:
        result += i


print result
