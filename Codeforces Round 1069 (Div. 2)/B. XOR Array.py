t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    arrayy = []
    previous = 0
    for i in range(1, n + 1):
        current  = l - 1 if i == r else i
        arrayy.append(current ^ previous)
        previous = current
    print(*arrayy)