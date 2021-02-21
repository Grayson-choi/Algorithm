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
cnt = 0
answer_list = [x for x in range(1, 10)]
result = "YES"
ck_list = [0] * 10

T = 9

for i in range(T):
    ck_list = [0] * 10
    num_list = list(map(int, input().split()))
    pan.append(num_list)

    for num in num_list:
        ck_list[num] = 1

    if sum(ck_list) != 9:
        result = "NO"


for col in list(zip(*pan)):
    ck_list = [0] * 10
    for num in col:
        ck_list[num] = 1

    if sum(ck_list) != 9:
        result = "NO"


for i in range(3):
    for j in range(3):
        ck_list = [0] * 10
        for x in range(3):
            for y in range(3):
                ck_list[pan[3 * i + x][3 * j + y]] = 1

        if sum(ck_list) != 9:
            result = "NO"

print(result)