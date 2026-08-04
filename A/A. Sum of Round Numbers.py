t = int(input())

for _ in range(t):
    n = int(input())
    numlist= []
    if n%1000 == 0:
            numlist.append(n//1000)
            print(n%1000)
            n = n - n//1000
    if n%100 == 0:
        numlist.append(n//100)
        n = n - n//100
    if n%10 == 0:
            numlist.append(n//10)
            n = n - n//10
    if n != 0:
         numlist.append(n)
    print(numlist)


