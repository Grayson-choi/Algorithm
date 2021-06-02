import sys
import pprint
sys.stdin = open("input2.txt", "r")

T = int(input())

def set_field(col, row, d1, d2):
    global board
    print("x", row, "y", col, "d1", d1, "d2", d2)

    for i in range(d1 + 1):
        if 0 <= row - i < n and 0 <= col + i < n:
            check_board[row - i][col + i] = "*"
        if 0 <= row + d2 - i < n and 0 <= col + d2 + i < n:
            check_board[row + d2 - i][col + d2 + i] = "*"

    for i in range(d2 + 1):
        if 0 <= row + i < n and 0 <= col + i < n and 0 <= row - d1 + i < n and 0 <= col + d1 + i < n:
            check_board[row + i][col + i] = "*"
            check_board[row - d1 + i][col + d1 + i] = "*"

    for row in check_board:
        indices = [i for i, x in enumerate(row) if x == "*"]
        # print(row)
        if len(indices) == 2:
            for index, value in enumerate(row):
                if indices[0] <= index <= indices[1]:
                    row[index] = "*"




def get_result(row, col, d1, d2):
    global check_board
    result_list = [0] * 5
    # 1번 구역 계산
    for y in range(n):
        for x in range(n):
            # print(y, x)
            if check_board[y][x] != "*":
                if 0 <= x <= col + d1 and 0 <= y <= row:
                    result_list[0] += board[y][x]
                    check_board[y][x] = 1
                    # print("1구역")

                elif 0 <= x <= col + d2 and row < y <= n:
                    result_list[1] += board[y][x]
                    check_board[y][x] = 2
                    # print("2구역")

                elif col + d1 <= x <= n and 0 <= y < row - d1 + d2:
                    result_list[2] += board[y][x]
                    check_board[y][x] = 3
                    # print("3구역")

                elif col + d2 <= x <= n and row - d1 + d2 <= y <= n:
                    result_list[3] += board[y][x]
                    check_board[y][x] = 4
                    # print("4구역")
            else:
                result_list[4] += board[y][x]

    return result_list


for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    check_board = [[0] * (n + 1) for _ in range(n + 1)]

    answer = 10 ** 6
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    # 1번 조건
                    if row + d1 + d2 > n:
                        continue
                    if col - d1 < 1:
                        continue
                    if col + d2 > n:
                        continue
                    set_field(col, row, d1, d2)
                    result_li = get_result(row, col, d1, d2)
                    result = max(result_li) - min(result_li)
                    if answer > result:
                        answer = result
    print(answer)
