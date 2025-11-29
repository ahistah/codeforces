string = str(input())

letters= []
count=0

for char in string:
    if char not in letters:
        count += 1
        letters.append(char)

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")