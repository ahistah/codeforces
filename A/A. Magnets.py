n= int(input())
numbers=[]
count=1

for i in range(n):
    numbers.append(str(input()))

for j in range(n-1):
    if numbers[j] != numbers[j+1]:
        count+=1

print(count)