import sys
import pprint
import queue
from collections import deque
import copy
sys.stdin = open('input.txt', "r")

T = int(input())

def check_airport(arr):
    global N, X

    result = 0
    front = -100
    back = -100

    visited = [0 for _ in range(N)]  # 활주로 완성된 거 정리

    for row in range(N):
        count = []  # 활주로 가능 여부를 계산 위한 리스트
        for col in range(N):
            now = arr[row][col]
            # print(row)
            if not count:
                count.append(now)

            # 같으면 넣음
            elif count[-1] == now:
                count.append(now)
            elif count[-1] - 1 == now:
                front = count[-1]
                # print(f"front 성립 {front}")
                count = [now]

            if len(count) == X:
                if front - 1 == now:
                    visited[row] = 1

            if count[-1] + 1 == now:
                # back = now
                if len(count) == X and front != back:  # 2 2 3 같은 경우
                    visited[row] = 1
                else:
                    count = [now]  # 2 3 인 경우 3으로 바꿈
            # print(count)

            if len(count) == N:  # 22222
                visited[row] = 1

            # 32223 X 안된다. + 1
            # 223 O


    print("v", visited)
    return sum(visited)



for tc in range(1, T + 1):
    N, X = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    board_col = list(map(list, zip(*board)))
    pprint.pprint(board)
    # pprint.pprint(board_col)
    row_result = check_airport(board)
    print("r", row_result)
    # col_result = check_airport(board_col)
    # print("c", col_result)
    # print(f"#{tc} {row_result + col_result}")
