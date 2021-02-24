import sys
import itertools
from pprint import pprint

"""
()(((()())(())()))(())
"""

"""
24
9983986983
"""

import sys
sys.stdin=open("input.txt", "r")

li = input()
stack = []
opened = 0
closed = 0
cnt = 0
for i in range(len(li)):
    if li[i] == "(":
        stack.append(li[i])
    else: # ")" 인경우
        stack.pop()
        if li[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)




