n= int(input())
gifts = list(map(int, input().split()))

gifters= [0]*n

for i in range(n):
    Pi= gifts[i]
    gifters[Pi-1]= i+1

print(*gifters)