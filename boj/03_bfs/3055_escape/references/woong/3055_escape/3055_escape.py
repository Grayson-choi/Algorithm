import sys
import pprint
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

def bfs(now):
    for i in range(4):


for tc in range(1, T + 1):
    R, C = map(int, input().split())
    forest = []
    start = (0, 0)
    end = (0, 0)
    for row in range(R):
        word = input()
        line = []
        for w in word:
            line.append(w)
        forest.append(line)
        if "S" in line:
            start_row, start_col = row, line.index("S")
        if "D" in line:
            end_row, end_col = row, line.index("D")


    print(start)
    print(end)
    pprint.pprint(forest)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
