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

    visited = [0 for _ in range(N)]  # 활주로 완성된 거 정리

    for row in range(N):
        count = []  # 활주로 가능 여부를 계산 위한 리스트
        front = -100
        for col in range(N):
            now = arr[row][col]
            # print(row)
            if not count:
                count.append(now)

            # 같으면 넣음
            elif count[-1] == now:
                count.append(now)

            # 2칸 내리막인경우
            elif count[-1] - 1 > now:
                visited[row] = 0
                continue

            # 1칸 내리막인경우
            elif count[-1] - 1 == now:
                if col + X > N:
                    # print(col, X, N)
                    # print("범위 초과")
                    visited[row] = 0
                    break
                else:
                    count = [now]
                    cnt = 0
                    for i in range(X):
                        if arr[row][col + i] == now:
                            cnt += 1
                    if cnt == X:
                        visited[row] = 1
                    else:
                        break
            # 오르막인 경우
            elif count[-1] + 1 == now:
                # back = now
                for i in range(col - X, col):  # 3 2 2 3 안됨
                    if arr[row][i] == count[-1] + 1:
                        count = [now]
                if len(count) == X:  # 2 2 3 같은 경우
                    visited[row] = 1
                else:
                    count = [now]  # 2 3 인 경우 3으로 바꿈
                    break

            if len(count) == N:  # 22222
                visited[row] = 1

            # print(count)

            # 32223 X 안된다. + 1
            # 223 O


    # print("v", visited)
    return sum(visited)



for tc in range(1, T + 1):
    N, X = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    board_col = list(map(list, zip(*board)))
    # rotate_G = [list(row) for row in zip(*board)]


    # pprint.pprint(board)
    # pprint.pprint(board_col)
    row_result = check_airport(board)
    # print("r", row_result)
    col_result = check_airport(board_col)
    # print("c", col_result)
    print(f"#{tc} {row_result + col_result}")
