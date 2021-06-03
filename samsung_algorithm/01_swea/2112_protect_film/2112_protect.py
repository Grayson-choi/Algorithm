import sys
import pprint
import queue
sys.stdin = open('input.txt', "r")

import copy
from itertools import combinations, product

T = int(input())

def check_flim(mylist):
    global k
    global m
    # 세로로 바꾸기
    check = [0] * m

    flag = False
    for idx, r in enumerate(list(map(list, zip(*mylist)))):
        count = []

        for element in r:
            if not count or count[0] == element:
                count.append(element)
            else:
                count = [element]

            if len(count) >= k:
                check[idx] = 1

        if check[idx] == 0:
            return False

        if sum(check) == m:
            return True



    return False


def change_board(board):
    global ab
    for t in range(2, k + 1):
        for AB in product((0, 1), repeat=t):
            case_list = list(combinations([x for x in range(n)], t))
            for case in case_list:
                maps = copy.deepcopy(board)
                for color_idx, row in enumerate(case):
                    for i in range(n):
                        if i == row:
                            ab_idx = AB[color_idx]
                            maps[i] = ab[ab_idx]
                rc = check_flim(maps)

                if rc:
                    an = len(case)
                    return an



for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    # print(f"#{tc}", n, m, k, "s")
    board = []
    dict = {}
    for _ in range(n):
        board.append(list(map(int, input().split())))
    # pprint.pprint(board)
    maps1 = copy.deepcopy(board)
    result = check_flim(maps1)
    ab = [[0] * m, [1] * m]
    # 체크해서 0이면 넘어감
    if result:
        print("#{} {}".format(tc, 0))
        continue
    else:
        # print("else 실행됨")
        answer = change_board(board)
        print("#{} {}".format(tc, answer))






