t= int(input())
running = True

for i in range(t):
    rounds = 0
    a, b, c = list(map(int, input().split()))
    while running == True: 
        if a == b or b == c or a == c:
            running = False
            break
        else:
            if a > b and a > c and b > c:
                a -= 1
                c += 1
                rounds += 1
            elif b > a and b > c:
                b -= 1
                c += 1
                rounds += 1
            else:
                c += 1
                b -= 1
                rounds += 1
    print(rounds)