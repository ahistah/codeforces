n, k = list(map(int, input().split()))
elements = list(map(int, input().split()))
count=0

for each in elements:
    if each >= elements[k-1] and each>0:
        count += 1

print(count)