n=int(input())
buff = n
a= []

while n > 1:
    if n%2 == 1:
        a.append("I love that")
        n -=1
    else:
        a.append("I hate that")
        n -=1

a.reverse()

if buff%2 == 0:
    a.append("I love it")
else:
    a.append("I hate it")

print(' '.join(a))