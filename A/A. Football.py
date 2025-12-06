position = str(input())
count0=0
count1=0

for char in position:
    if char == "0":
        count1= 0
        count0 += 1
    else:
        count0 = 0
        count1 += 1
    if count0 >= 7 or count1 >=7:
        break

if count0 >= 7 or count1 >=7:
    print("YES")
else:
    print("NO")