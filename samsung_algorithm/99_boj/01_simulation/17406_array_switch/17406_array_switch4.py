

n, m, k = map(int, input().split())

board = []
operations = []


def switch(r, c, s):
    global board
    start, end, center = (r - s, c - s), (r + s, c + s), (s, r)

    for i in range(1, s + 1):
        center_row, center_col = center[0], center[1]
        print("c", center_row, center_col)
        # start_row, start_col = start[0] - 1, start[1] - 1
        # end_row, end_col = end[0] - 1, end[1] - 1


        size = i * 2
        temp = 0
        start_row, start_col = center_row - i, center_col - i
        end_row, end_col = center_row + i, center_col + i
        print("s", start_row, start_col)
        print("e", end_row, end_col)
        # 상
        print("상끝", start_col + size)
        idx = 1
        for i in range(start_col, start_col + size):
            print(i)
            board[start_row][start_col + 1] = board[start_row][i]
            print(board)
        # 오
        # 하
        # 좌










for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(k):
    operation = list(map(int, input().split()))
    operations.append(operation)

    r, c, s = operations[i]
    switch(r, c, s)





