from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    distinct = len(freq)
    odd_count = sum(1 for c in freq.values() if c % 2 == 1)
    even_count = distinct - odd_count

    # Special case: only 1 distinct element
    if distinct == 1:
        print(2 if n % 2 == 1 else 0)
        continue

    # Special case: only 2 distinct elements
    if distinct == 2:
        if n % 2 == 1:
            print(2)
        else:
            # Both even freq → can get 4, otherwise just odd_count
            print(4 if even_count == 2 else odd_count)
        continue

    # General case
    if distinct > n:
        # More distinct elements than slots
        # Can only use n distinct elements, prioritize odd-freq ones
        usable_evens = min(even_count, max(0, n - odd_count))
        ans = odd_count + 2 * usable_evens
    else:
        # All distinct elements must appear in both
        ans = min(2 * distinct, odd_count + 2 * even_count)

    # Parity constraint
    if ans % 2 != odd_count % 2:
        ans -= 1

    print(ans)
