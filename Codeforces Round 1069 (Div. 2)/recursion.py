import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        t = int(next(iterator))
    except StopIteration:
        return

    output = []
    
    for _ in range(t):
        try:
            n = int(next(iterator))
            l = int(next(iterator))
            r = int(next(iterator))
        except StopIteration:
            break
        
        # We construct the array 'a' based on the prefix sum array P where:
        # P[i] = i for all i != r
        # P[r] = l - 1
        # This ensures only the subarray [l, r] has XOR sum 0.
        
        # Base array construction: a[i] = (i+1) ^ i
        # This corresponds to P[k] = k for all k.
        # We use 0-based indexing for the list 'a', so index i corresponds to problem index i+1.
        a = [i ^ (i - 1) for i in range(1, n + 1)]
        
        # Fix values around index r (problem index).
        # In 0-based list 'a', this is index r-1.
        
        # a_r = P[r] ^ P[r-1]
        # P[r] is set to (l-1)
        # P[r-1] is (r-1)
        a[r-1] = (l - 1) ^ (r - 1)
        
        # a_{r+1} = P[r+1] ^ P[r]
        # Only exists if r < n
        if r < n:
            # P[r+1] is (r+1)
            # P[r] is (l-1)
            a[r] = (r + 1) ^ (l - 1)
            
        output.append(" ".join(map(str, a)))

    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()