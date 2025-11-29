y = int(input())
flag=False

for i in range(y+1, 100000):
    char = str(i)
    if len(char) == len(set(char)):
        print(i)
        break
