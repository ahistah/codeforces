n = str(input())
luck_count=0

for char in n:
    if char == '7' or char == '4':
        luck_count += 1

if luck_count == 7 or luck_count == 4:
    print("YES")
else:
    print("NO")
