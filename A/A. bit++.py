n = int(input())
y=0

def add(num):
    num +=1
    return num

def subtract(num):
    num -=1
    return num

for i in range(n):
    line = str(input())
    flag = False
    for char in line:
        if char == "+":
            flag = True
    if flag == True:
        y= add(y)
    else:
        y= subtract(y)

print(y)