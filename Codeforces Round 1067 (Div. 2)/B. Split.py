#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from collections import Counter

def main():
    def solve():
        n = int(input())
        a = list(map(int, input().split()))
        freq = Counter(a)
        distinct = len(freq)
        odd_count = sum(1 for f in freq.values() if f % 2 == 1)
        even_count = distinct - odd_count
        if distinct == 1:
            print(2 if n % 2 == 1 else 0)
            return
        if distinct == 2:
            if n % 2 == 1:
                # With odd n and 2 elements, one must be odd count, one even in each subsequence
                print(2)
            else:
                # With even n and 2 elements, check if we can make both odd in both
                # This is only possible if both frequencies are even
                # Because with even n, we need a+b = n where both a,b are odd (impossible!)
                # OR we need to split cleverly...
                # Actually if both have even total freq, we can potentially get 4
                # If any has odd freq, we get just the odd_count
                print(4 if even_count == 2 else odd_count)
            return
        if distinct > n:
            usable_evens = min(even_count, max(0, n - odd_count))
            max_val = odd_count + 2 * usable_evens
        else:
            max_val = min(2 * distinct, odd_count + 2 * even_count)
        if max_val % 2 != odd_count % 2:
            max_val -= 1
        print(max_val)
    t = int(input())
    for _ in range(t):
        solve()



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()