import sys
import itertools
from pprint import pprint

"""
(3+5)*2
"""

"""
35+2*
"""

import sys
sys.stdin=open("input.txt", "r")
import collections
n, K = map(int, input().split())
li = [x for x in range(1, n + 1)]
q = []
while li:
    for j in range(K - 1):
        element = li.pop(0)
        li.append(element)
    li.pop(0)
    if len(li) == 1:
        print(li[0])


