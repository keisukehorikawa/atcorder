# https://atcoder.jp/contests/abc167/tasks/abc167_a
# A - Registration

import io
import sys

_INPUT = """\
chokudai
chokudaiz
"""

sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()
if S == T[0:-1]:
    print('Yes')
else:
    print('No')