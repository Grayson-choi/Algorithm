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
3
2 0 3
5 1 2
3 1 4

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
    if direction == 0:
        for _ in range(index):
            pan[row - 1].append(pan[row - 1].pop(0))
    else:
        for _ in range(index):
            pan[row - 1].insert(0, pan[row - 1].pop())

for i, num_list in enumerate(pan):
    if i == 0:
        left = 0
        right = T
        number = num_list[left:right + 1]
        total += sum(number)
    elif i <= int(T//2):
        left += 1
        right -= 1
        number = num_list[left:right]
        total += sum(number)
    else:
        left -= 1
        right += 1
        number = num_list[left:right]
        total += sum(number)

print(total)