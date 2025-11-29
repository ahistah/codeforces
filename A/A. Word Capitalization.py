stringy= input()
lst=[]

for char in stringy:
    lst.append(char)

lst[0]= lst[0].upper()

print(''.join(lst))