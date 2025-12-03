n, m, a = list(map(int, input().split()))
tiles =0
vertical=0
horizontal=0

if n % a != 0:
    vertical += n//a +1
else:
    vertical += n//a

if m % a != 0:
    horizontal += m//a +1
else:
    horizontal += m//a

tiles= vertical*horizontal

print(tiles)