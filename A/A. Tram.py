n = int(input())
people=0
max=0

for i in range(n):
    a, b= list(map(int, input().split()))
    people += b-a
    if people > max:
        max = people

print(max)