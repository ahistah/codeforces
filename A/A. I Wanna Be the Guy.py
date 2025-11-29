n= int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
flag= "I become the guy."

p.pop(0)
q.pop(0)

pq= p + q
pq= set(pq)
pq= sorted(pq)
pq= list(pq)

for i in range(n):
    if len(pq)>= n:
        if pq[i] != i+1:
            flag= "Oh, my keyboard!"
    else:
        flag = "Oh, my keyboard!"
print(flag)

