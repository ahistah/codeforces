t= int(input())

for i in range(t):
    count=0
    a, b= list(map(int, input().split()))
    remainder = a%b
    if remainder !=0:
        count= b-remainder
    print(count)

