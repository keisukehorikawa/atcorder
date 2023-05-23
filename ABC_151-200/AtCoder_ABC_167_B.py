# https://atcoder.jp/contests/abc167/tasks/abc167_b
# B - Easy Linear Programming

import io
import sys

_INPUT = """\
2000000000 0 0 2000000000
"""

sys.stdin = io.StringIO(_INPUT)

A, B, C, K = map(int, input().split())

if A >= K:
    ans = K
elif K - A <= B:
    ans = A
else:
    ans = A - (K - A - B)

print(ans)