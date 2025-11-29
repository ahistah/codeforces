x = int(input())
step=0

while x != 0:
    if x - 5 >= 0:
        x -= 5
    elif x - 4 >= 0:
        x -= 4
    elif x - 3 >= 0:
        x -= 3
    elif x - 2 >= 0:
        x -= 2
    else:
        x -= 1
    step += 1

print(step)