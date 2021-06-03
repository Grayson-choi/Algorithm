import sys
import pprint
import queue
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(input())


for tc in range(1, T + 1):
    pass

    n = int(input())
    # arr = [list(map(int, input().split()) for _ in range(n)]

    board = [list(map(int, input().split())) for _ in range(n)]
    # check_board = [[0] * (n + 1) for _ in range(n + 1)]