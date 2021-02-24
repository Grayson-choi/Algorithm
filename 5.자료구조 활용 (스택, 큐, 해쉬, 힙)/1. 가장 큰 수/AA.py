import sys
import itertools
from pprint import pprint

"""
948096783986983 5
"""

"""
24
9983986983
"""

import sys
# sys.stdin=open("input.txt", "r")

import sys
sys.stdin=open("input.txt", "r")

num, target = map(int, input().split())
nums = list(map(int, str(num)))
print(nums)
stack=[]
for x in nums:
    while stack and target > 0 and stack[-1] < x:
        stack.pop()
        target -= 1
    stack.append(x)
if target != 0:
    stack = stack[:-target]

result = "".join(map(str, stack))
print(result)















