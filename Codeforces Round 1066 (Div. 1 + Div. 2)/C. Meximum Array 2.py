t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    constraints = []
    for _ in range(q):
        c, l, r = map(int, input().split())
        constraints.append((c, l - 1, r - 1))  # Convert to 0-indexed

    # Initialize array
    ans = [10**9] * n

    # Separate constraints
    mex_ranges = [(l, r) for c, l, r in constraints if c == 2]
    min_ranges = [(l, r) for c, l, r in constraints if c == 1]

    # Mark which positions are in MEX ranges
    in_mex = [False] * n
    for l, r in mex_ranges:
        for i in range(l, r + 1):
            in_mex[i] = True

    # Mark which positions are in MIN ranges
    in_min = [False] * n
    for l, r in min_ranges:
        for i in range(l, r + 1):
            in_min[i] = True

    # Set positions that are in MIN but NOT in MEX to k
    # (these are safe places to put k)
    for l, r in min_ranges:
        has_k = False
        for i in range(l, r + 1):
            if not in_mex[i]:
                ans[i] = k
                has_k = True
                break

    # Set positions that are in BOTH MIN and MEX to k+1
    # (must be >= k for MIN, must be != k for MEX, so k+1)
    for i in range(n):
        if in_min[i] and in_mex[i]:
            ans[i] = k + 1

    # Now place values 0 to k-1 for MEX constraints
    for l, r in mex_ranges:
        needed = list(range(k))

        # Check what values are already present
        present = set()
        for i in range(l, r + 1):
            if 0 <= ans[i] < k:
                present.add(ans[i])

        # Filter out present values
        needed = [v for v in needed if v not in present]

        # Place the missing values in positions that are not in MIN ranges
        for val in needed:
            for i in range(l, r + 1):
                if not in_min[i] and ans[i] >= k:
                    ans[i] = val
                    break

    print(*ans)

#THIS IS A WRONG SOLUTION, ONLY WORKS FOR A SINGLE TEST CASE !! INT BLOWS UP !!