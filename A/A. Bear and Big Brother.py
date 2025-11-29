a, b = list(map(int, input().split()))
time=0

while a <= b:
    a *= 3
    b *= 2
    time += 1

print(time)





