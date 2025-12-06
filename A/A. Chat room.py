s = str(input())
reference= "hello"
j=0

for char in s:
    if char == reference[j]:
        j+=1
        if j == len(reference):
            break

if j == len(reference):
    print("YES")
else:
    print("NO")