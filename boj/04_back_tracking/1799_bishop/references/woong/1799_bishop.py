import sys
import pprint
sys.stdin = open("input.txt", "r")

def check_bishop(row, col):
    if board[row][col] == 0:
        check[row][col] = 100000
    for i in range(1, N + 1):
        up_row = row + i
        down_row = row - i
        left_col = col - i
        right_col = col + i
        if 0 <= up_row < N and 0 <= right_col < N:
            # print(board[up_row][right_col])
            if board[up_row][right_col] == 1:
                check[row][col] += 1
        if 0 <= down_row < N and 0 <= right_col < N:
            # print(board[down_row][right_col])
            if board[down_row][right_col] == 1:
                check[row][col] += 1
        if 0 <= down_row < N and 0 <= left_col < N:
            # print(board[down_row][left_col])
            if board[down_row][left_col] == 1:
                check[row][col] += 1
        if 0 <= up_row < N and 0 <= left_col < N:
            # print(board[up_row][left_col])
            if board[up_row][left_col] == 1:
                check[row][col] += 1


def check_cross(row, col):
    global board

    for i in range(1, N):
        up_row = row + i
        down_row = row - i
        left_col = col - i
        right_col = col + i

        if 0 <= up_row < N and 0 <= right_col < N:
            board[up_row][right_col] = 0
        if 0 <= down_row < N and 0 <= right_col < N:
            board[down_row][right_col] = 0
        if 0 <= down_row < N and 0 <= left_col < N:
            board[down_row][left_col] = 0
        if 0 <= up_row < N and 0 <= left_col < N:
            board[up_row][left_col] = 0


def find_min():
    global min_row
    global min_col
    min = 999999
    for row in range(N):
        for col in range(N):
            if check[row][col] <= min:
                min = check[row][col]
                min_row = row
                min_col = col
    return min_row, min_col

N = int(input())
cnt = 0
board = []
check = [[0] * N for _ in range(N)]

for i in range(N):
    board.append(list(map(int, input().split())))
# pprint.pprint(board)

# 가장 좋은 bishop 위치 찾기
for row in range(N):
    for col in range(N):
        check_bishop(row, col)
pprint.pprint(check)

for _ in range(N*N):
    bishop_row, bishop_col = find_min()
    print("min", bishop_row, bishop_col)
    # print("board", board[bishop_row][bishop_col])
    if board[bishop_row][bishop_col] == 0:
        check[bishop_row][bishop_col] = 100000
        continue
    if board[bishop_row][bishop_col] == 1:
        check[bishop_row][bishop_col] = 999999
        check_cross(bishop_row, bishop_col)
        board[bishop_row][bishop_col] = 0
        # pprint.pprint(check)
        print("--------")
        pprint.pprint(board)
        # print("--------")
        cnt += 1

print(cnt)

