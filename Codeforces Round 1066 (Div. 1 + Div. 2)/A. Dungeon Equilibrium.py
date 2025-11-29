t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_num = max(a)
    counter = 0
    for j in range(max_num + 1):
        instances = a.count(j)
        if instances > j:
            counter += (instances - j)
        elif instances < j:
            counter += instances 
    print(counter)
