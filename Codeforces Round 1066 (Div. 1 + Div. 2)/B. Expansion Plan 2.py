t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    s = str(input().strip())

    eight_shift = s.count('8')
    four_shift = s.count('4')

    delta_x = max(0, abs(x) - eight_shift)
    delta_y = max(0, abs(y) - eight_shift)

    if delta_x + delta_y <= four_shift:
        print("YES")
    else:
        print("NO")

#essentially the square will overwrite the diamond so this is more efficient, we just use the difference

#using manhattan and chebshev distances logic, manhattan distance must cover the difference, geometrical solution