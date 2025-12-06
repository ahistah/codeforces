t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    previous = 0
    for i in range(1, n + 1):
        current = l - 1 if i == r else i
        a.append(current ^ previous)
        previous = current
    print(*a)