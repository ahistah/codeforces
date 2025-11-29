n, h= list(map(int, input().split()))

heights= list(map(int, input().split()))

count = n

for i in range(n):
    if heights[i] > h:
        count += 1
    
print(count)