n = int(input())

s= str(input())

characters=[]
count=0

for char in s:
    characters.append(char)

for i in range(n-1):
    if characters[i] == characters[i+1]:
        count +=1

print(count)