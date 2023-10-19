import sys
sys.setrecursionlimit(100000)

MOD = 10**9 + 7
m = {}

def recursion(a, b, c, n):
    if n == 0:
        return a
    if n < 0:
        return 0
    if n in m:
        return m[n]

    m[n] = (recursion(a, b, c, n - 1) + b * recursion(a, b, c, n - 2) + c) % MOD
    return m[n]

a, b, c, n = map(int, input().split())
print(recursion(a, b, c, n))

