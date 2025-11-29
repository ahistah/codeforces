#n=(sum of digits of n)**2

results = []

for i in range(1, 999999999999):
    s = sum(int(d) for d in str(i))
    if i == s ** 2:
        results.append(i)

print(results)

