k, n, w = list(map(int, input().split()))

cost=0
borrow=0

for i in range(w+1):
    cost += k*i

if cost > n:
    borrow= cost-n

print(borrow)