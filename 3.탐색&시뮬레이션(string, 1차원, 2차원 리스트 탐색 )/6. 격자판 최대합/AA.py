import sys
import itertools
from pprint import pprint

"""
10
1 10 27 39 50 61 65 70 93 93 
7
7 51 65 66 70 82 93 
"""
#
# sys.stdin = open("input.txt", "rt")
pan = []
max = 0

T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    if sum(num_list) > max:
        max = sum(num_list)
    pan.append(num_list)


for col in list(zip(*pan)):
    if sum(col) > max:
        max = sum(col)

total1 = 0
total2 = 0
for i in range(len(pan)):
    total1 += pan[i][i]
    total2 += pan[-i][-i]

if total1 > max:
    max = total1
elif total2 > max:
    max = total2

print(max)

# for _ in range(10):
#     start, end = map(int, input().split())
#     start_list = nums[:start - 1]
#     middle_list = list(reversed(nums[start - 1:end]))
#     end_list = nums[end:]
#     nums = [*start_list, *middle_list, *end_list]
#
# print(" ".join(list(map(str, nums))))