n= int(input())
s= str(input())
a_count=0
d_count=0

for char in s:
    if char == 'A':
        a_count += 1
    else:
        d_count += 1

if a_count > d_count:
    print("Anton")
elif a_count < d_count:
    print("Danik")
else:
    print("Friendship")