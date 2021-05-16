import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint


def tornado(cor, dir):
    global result
    row, col = cor[0], cor[1]
    sand = table[row][col]
    table[row][col] = 0

    sand_01 = int(sand * 0.01)
    sand_02 = int(sand * 0.02)
    sand_05 = int(sand * 0.05)
    sand_07 = int(sand * 0.07)
    sand_10 = int(sand * 0.10)
    sand_45 = sand - (2 * (sand_01 + sand_02 + sand_07 + sand_10) + sand_05)
    if dir % 4 == 0:  # <- left 방향
        # 맨위
        if 0 <= row - 2 < N:
            table[row - 2][col] += sand_02
        else:
            result += sand_02
        # 2번째 row
        if 0 <= row - 1 <= N and 0 <= col - 1 < N:
            table[row - 1][col - 1] += sand_10
        else:
            result += sand_10
        if 0 <= row - 1 <= N:
            table[row - 1][col] += sand_07
        else:
            result += sand_07
        if 0 <= row - 1 <= N and 0 <= col + 1 < N:
            table[row - 1][col + 1] += sand_01
        else:
            result += sand_01

        # 3번째 row
        if 0 <= col - 2 < N:
            table[row][col - 2] += sand_05
        else:
            result += sand_05
        if 0 <= col - 1 < N:
            table[row][col - 1] += sand_45
        else:
            result += sand_45
        # 4번째 row
        if 0 <= row + 1 < N and 0 <= col - 1 < N:
            table[row + 1][col - 1] += sand_10
        else:
            result += sand_10
        if 0 <= row + 1 < N:
            table[row + 1][col] += sand_07
        else:
            result += sand_07
        if 0 <= row + 1 < N and 0 <= col + 1 < N:
            table[row + 1][col + 1] += sand_01
        else:
            result += sand_01
        # 5번째 row
        if 0 <= row + 2 < N:
            table[row + 2][col] += sand_02
        else:
            result += sand_02

    elif dir % 4 == 1:  # down
        # 1번 row
        if 0 <= row - 1 <= N and 0 <= col - 1 < N:
            table[row - 1][col - 1] += sand_01
        else:
            result += sand_01
        if 0 <= row - 1 <= N and 0 <= col + 1 < N:
            table[row - 1][col + 1] += sand_01
        else:
            result += sand_01
        # 2번 row
        if 0 <= col - 2 < N:
            table[row][col - 2] += sand_02
        else:
            result += sand_02
        if 0 <= col - 1 < N:
            table[row][col - 1] += sand_07
        else:
            result += sand_07

        if 0 <= col + 1 < N:
            table[row][col + 1] += sand_07
        else:
            result += sand_07

        if 0 <= col + 2 < N:
            table[row][col + 2] += sand_02
        else:
            result += sand_02
        # 3번째
        if 0 <= row + 1 < N and 0 <= col - 1 < N:
            table[row + 1][col - 1] += sand_10
        else:
            result += sand_10
        if 0 <= row + 1 < N:
            table[row + 1][col] += sand_45
        else:
            result += sand_45
        if 0 <= row + 1 < N and 0 <= col + 1 < N:
            table[row + 1][col + 1] += sand_10
        else:
            result += sand_10
        # 5번째 row
        if 0 <= row + 2 < N:
            table[row + 2][col] += sand_05
        else:
            result += sand_05

    elif dir % 4 == 2:  # right
        # 맨위
        if 0 <= row - 2 < N:
            table[row - 2][col] += sand_02
        else:
            result += sand_02
        # 2번째 row (오른쪽이니까 반대로)
        if 0 <= row - 1 <= N and 0 <= col - 1 < N:
            table[row - 1][col - 1] += sand_01
        else:
            result += sand_01
        if 0 <= row - 1 <= N:
            table[row - 1][col] += sand_07
        else:
            result += sand_07
        if 0 <= row - 1 <= N and 0 <= col + 1 < N:
            table[row - 1][col + 1] += sand_10
        else:
            result += sand_10

        # 3번째 row
        if 0 <= col + 2 < N:
            table[row][col + 2] += sand_05
        else:
            result += sand_05
        if 0 <= col + 1 < N:
            table[row][col + 1] += sand_45
        else:
            result += sand_45
        # 4번째 row
        if 0 <= row + 1 < N and 0 <= col - 1 < N:
            table[row + 1][col - 1] += sand_01
        else:
            result += sand_01
        if 0 <= row + 1 < N:
            table[row + 1][col] += sand_07
        else:
            result += sand_07
        if 0 <= row + 1 < N and 0 <= col + 1 < N:
            table[row + 1][col + 1] += sand_10
        else:
            result += sand_10
        # 5번째 row
        if 0 <= row + 2 < N:
            table[row + 2][col] += sand_02
        else:
            result += sand_02

    elif dir % 4 == 3:  # up
        # 1번 row
        if 0 <= row - 2 < N:
            table[row - 2][col] += sand_05
        else:
            result += sand_05
        # 2번 row
        if 0 <= row - 1 <= N and 0 <= col - 1 < N:
            table[row - 1][col - 1] += sand_10
        else:
            result += sand_10
        if 0 <= row - 1 < N:
            table[row - 1][col] += sand_45
        else:
            result += sand_45
        if 0 <= row - 1 <= N and 0 <= col + 1 < N:
            table[row - 1][col + 1] += sand_10
        else:
            result += sand_10
        # 2번 row
        if 0 <= col - 2 < N:
            table[row][col - 2] += sand_02
        else:
            result += sand_02
        if 0 <= col - 1 < N:
            table[row][col - 1] += sand_07
        else:
            result += sand_07

        if 0 <= col + 1 < N:
            table[row][col + 1] += sand_07
        else:
            result += sand_07
        if 0 <= col + 2 < N:
            table[row][col + 2] += sand_02
        else:
            result += sand_02
        # 3번째
        if 0 <= row + 1 < N and 0 <= col - 1 < N:
            table[row + 1][col - 1] += sand_01
        else:
            result += sand_01

        if 0 <= row + 1 < N and 0 <= col + 1 < N:
            table[row + 1][col + 1] += sand_01
        else:
            result += sand_01
        # 5번째 row
    # pprint(table)
    # print("r", result)

# 토네이도 패턴
# 1 - 2 - 3 - 3 - 4 - 4 - 1 - 1 - 1 - 2 - 2 - 2


N = int(input())
result = 0
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# 토네이도 경로
# (2,2) -> (2,1) col: -1
# (2,1) -> (3,1) row: +1
# (3,1) -> (3,3) col: +2
# (3,3) -> (1,3) row: -2
# (1,3) -> (1,0) col: -3
# (1,0) -> (4,0) row: +3
# (4,0) -> (4,4) col: +4
# (4,4) -> (0,4) row: -4
# (0,4) -> (0,0) col: -4
start_row, start_col = N // 2, N // 2
end_row, end_col = N // 2, N // 2
# print(f"start: {start_row} {start_col}")
dir = 0
for i in range(1, N):
    if i % 2 == 1:

        for j in range(1, i + 1):
            start_col -= 1
            # print(f"{dir}: ", start_row, start_col)
            tornado((start_row, start_col), dir)
        dir += 1
        for j in range(1, i + 1):
            start_row += 1
            # print(f"{dir}: ", start_row, start_col)
            tornado((start_row, start_col), dir)
        dir += 1
    else:
        for j in range(1, i + 1):
            start_col += 1
            # print(f"{dir}: ", start_row, start_col)
            tornado((start_row, start_col), dir)
        dir += 1
        for j in range(1, i + 1):
            start_row -= 1
            # print(f"{dir}: ", start_row, start_col)
            tornado((start_row, start_col), dir)
        dir += 1

for _ in range(N - 1):
    start_col -= 1
    # print(f"{dir}: ", start_row, start_col)
    tornado((start_row, start_col), dir)
# dir += 1
print(result)



