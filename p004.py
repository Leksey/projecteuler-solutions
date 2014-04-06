palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        y = str(x)
        if y == y[::-1]:
            palindromes.append(x)
        j +=1
palindromes.sort()
print palindromes[-1]