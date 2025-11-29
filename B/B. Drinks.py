n= int(input())
sum=0
drinks= list(map(int, input().split()))

for element in drinks:
    sum+=element

print(sum/n)