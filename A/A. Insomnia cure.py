k= int(input())
l= int(input())
m= int(input())
n= int(input())
d= int(input())

dragons= [0]*d

for a in range(k-1, d, k):
    dragons[a]=1

for a in range(l-1, d, l):
    dragons[a]=1

for a in range(m-1, d, m):
    dragons[a]=1

for a in range(n-1, d, n):
    dragons[a]=1

print(dragons.count(1))