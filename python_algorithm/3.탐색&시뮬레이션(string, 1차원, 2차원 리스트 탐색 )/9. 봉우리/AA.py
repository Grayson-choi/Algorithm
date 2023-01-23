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


T = int(input())
pan.append([0] * (T + 2))
for i in range(T):
    num_list = [0, *list(map(int, input().split())), 0]
    pan.append(num_list)

pan.append([0] * (T + 2))

for x in range(1, T + 1):
    for y in range(1, T + 1):
        if pan[x - 1][y] < pan[x][y] and pan[x + 1][y] < pan[x][y] and pan[x][y + 1] < pan[x][y] and pan[x][y - 1] < pan[x][y]:
            cnt += 1
print(cnt)