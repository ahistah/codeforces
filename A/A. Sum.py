t= int(input())

for _ in range(t):
    a, b, c = list(map(int, input().split()))
    flag = "NO"
    #a + b = c
    if a + b == c:
        flag = "YES"
    elif b + c == a:
        flag = "YES"
    elif a + c == b:
        flag = "YES"
    print(flag)
