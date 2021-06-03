# row : 가로 길이 n
# col : 세로 길이 m

# board = [[0 for i in range(COLUM)] for j in range(ROW)]



# 2차원 배열 가장 자리에 0 추가하는 코드
# n은 배열의 크기
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0, 0)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):  # 4방향 탐색해서 가운데 값이 제일 높다면!
            cnt += 1
print(cnt)


def set_field(row, col, d1, d2):
    global board
    # print("x", row, "y", col, "d1", d1, "d2", d2)

    # start point 는 [row][col]
    # check_board[row][col] 대각선 위로 d1 길이만큼 별그리기
    for i in range(d1 + 1):
        if 0 <= row - i < n and 0 <= col + i < n:
            check_board[row - i][col + i] = "*"
        # check_board start_point에서 대각선 아래 d2 만큼 이동한 곳에서 대각선 위로 별그리기
        if 0 <= row + d2 - i < n and 0 <= col + d2 + i < n:
            check_board[row + d2 - i][col + d2 + i] = "*"

    # 대각선 아래로 그림 그리기
    for i in range(d2 + 1):
        if 0 <= row + i < n and 0 <= col + i < n:
            check_board[row + i][col + i] = "*"

        if 0 <= row - d1 + i < n and 0 <= col + d1 + i < n:
            check_board[row - d1 + i][col + d1 + i] = "*"
    pprint.pprint(check_board)