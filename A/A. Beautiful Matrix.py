line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
line4 = list(map(int, input().split()))
line5 = list(map(int, input().split()))

i= 0
j= 0

if 1 in line1:
    i= 1
    j= line1.index(1) + 1

if 1 in line2:
    i= 2
    j= line2.index(1) + 1


if 1 in line3:
    i= 3
    j= line3.index(1) + 1

if 1 in line4:
    i= 4
    j= line4.index(1) + 1

if 1 in line5:
    i= 5
    j= line5.index(1) + 1

horizontal = abs(j - 3)
vertical = abs(i - 3)

movement= horizontal + vertical

print(movement)