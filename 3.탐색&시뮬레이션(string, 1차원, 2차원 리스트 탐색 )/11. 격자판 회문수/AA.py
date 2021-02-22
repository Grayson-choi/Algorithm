import sys
import itertools
from pprint import pprint

"""
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1 
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

"""
#
# sys.stdin = open("input.txt", "rt")
pan = []
cnt = 0

for _ in range(7):
    pan.append(list(map(int, input().split())))

r_pan = list(map(list, zip(*pan)))

for i in range(7):
    for j in range(3):
        line = pan[i][j:j+5]
        col = r_pan[i][j:j+5]
        if line == line[::-1] or col == col[::-1]:
            cnt += 1

print(cnt)