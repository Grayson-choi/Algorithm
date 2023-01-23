import sys
import itertools
from pprint import pprint

"""
15 99
73 32 31 49 94 37 40 62 78 66 27 100 99 29 9 

"""
#
# sys.stdin = open("input.txt", "rt")

n, target = map(int, input().split())
nums = sorted(map(int, input().split()))

print(nums.index(target) + 1)