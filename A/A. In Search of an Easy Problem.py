n = int(input())
count=0

numbers= list(map(int, input().split()))

for element in numbers:
    if element == 1:
        count += 1

if count > 0:
    print("Hard")
else:
    print("Easy")