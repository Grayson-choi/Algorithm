import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
"""
#
# sys.stdin = open("input.txt", "rt")

nums = [x for x in range(1, 20 + 1)]

for _ in range(10):
    start, end = map(int, input().split())
    start_list = nums[:start - 1]
    middle_list = list(reversed(nums[start - 1:end]))
    end_list = nums[end:]
    nums = [*start_list, *middle_list, *end_list]

print(" ".join(list(map(str, nums))))
