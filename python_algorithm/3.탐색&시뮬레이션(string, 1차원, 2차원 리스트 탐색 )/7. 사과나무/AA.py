import sys
import itertools
from pprint import pprint

"""
7
74 10 31 26 59 16 89
78 44 49 1 64 33 15
9 95 70 18 22 25 40
62 77 28 3 78 75 23
82 38 20 16 42 1 79
1 24 2 25 95 26 79
4 35 46 94 70 44 83
"""
#
# sys.stdin = open("input.txt", "rt")
pan = []
total = 0
left = 0
right = 0

T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    pan.append(num_list)



change_num = int(input())
for i in range(change_num):
    row, direction, index = map(int, input().split())
    change_list = pan[row]
    if direction == 0:
        left = pan[row][:index]
        right = pan[row][index:]
        print(left, right)
        pan[row] = [*right, *left]
    else:
        left = pan[row][:index - 1]
        right = pan[row][index - 1:]
        print(left, right)
        pan[row] = [*right, *left]


for i,num_list in enumerate(pan):
    if i == 0:
        left = 0
        right = T
        number = num_list[left:right + 1]
        total += sum(number)
        # print(left, right)
        # print(num_list[left])
    elif i < int(T//2):
        left += 1
        right -= 1
        number = num_list[left:right + 1]
        total += sum(number)
        # print(left, right)
        # print(number)
    else:
        left -= 1
        right += 1
        # print(left, right)
        number = num_list[left:right + 1]
        total += sum(number)
        # print(number)

print(total)

# for _ in range(10):
#     start, end = map(int, input().split())
#     start_list = nums[:start - 1]
#     middle_list = list(reversed(nums[start - 1:end]))
#     end_list = nums[end:]
#     nums = [*start_list, *middle_list, *end_list]
#
# print(" ".join(list(map(str, nums))))