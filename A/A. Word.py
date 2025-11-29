s = str(input())
upper=0
lower=0

for char in s:
    if char.isupper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    string= s.upper()
else:
    string= s.lower()

print(string)