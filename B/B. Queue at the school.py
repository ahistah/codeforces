n, t = list(map(int, input().split()))
s= str(input())
people= list(s)


for i in range(t):
    i=0    
    while i < n-1:
        if people[i] < people[i+1]: #unicode index comparison
            people[i], people[i+1]= people[i+1], people[i]
            i += 1
        i += 1

a= "".join(people)

print(a)
