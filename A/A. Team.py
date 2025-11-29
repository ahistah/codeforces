n = int(input())
solution = 0

for i in range(n):
    count= 0
    confidence=str(input())
    for binary in confidence:
        if binary == "1":
            count += 1
    if count >= 2:
        solution += 1

print(solution)

