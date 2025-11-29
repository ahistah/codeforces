import sys
from collections import Counter

# Set recursion depth just in case, though not needed here
sys.setrecursionlimit(2000)

def solve():
    # Use fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    iterator = iter(data)
    num_test_cases = int(next(iterator))
    
    results = []
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        a = []
        for _ in range(2 * n):
            a.append(int(next(iterator)))

        freq = Counter(a)
        
        odd_freq_count = 0
        even_freq_count = 0
        
        for count in freq.values():
            if count % 2 == 1:
                odd_freq_count += 1
            else:
                even_freq_count += 1
        
        # Base calculation:
        # Each odd-freq number adds 1 to the score.
        # Each even-freq number adds 2 to the score.
        ans = odd_freq_count + (2 * even_freq_count)
        
        # Parity Check:
        # If we have NO odd-freq numbers, we cannot adjust the partition sizes freely.
        # We must ensure the number of elements split 1-1 matches the target size n parity-wise.
        if odd_freq_count == 0:
            if even_freq_count % 2 != n % 2:
                ans -= 2
        
        results.append(str(ans))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()