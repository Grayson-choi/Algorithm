import pprint
import queue
from collections import deque
import copy
import sys

sys.stdin = open('input.txt', "r")

T = int(input())

# 8가지 방향에 대한 정의
dirs = {
    1: (-1, 0),  # 1 위↑
    2: (-1, -1),  # 2 왼위↖
    3: (0, -1),  # 3 왼←
    4: (1, -1),  # 4 왼아래↙
    5: (1, 0),  # 5 아래 ↓,
    6: (1, 1),  # 6 오른아래↘,
    7: (0, 1),   # 7 오른 →,
    8: (-1, 1),   # 8 오른 위 ↗
}

def find_fish_location(board, fish_num):
    for row in range(4):
        for col in range(4):
            if board[row][col][0] == fish_num:
                return (row, col)
    return None



def all_fish_move(board, fish_list, shark_loc):
    global dirs

    # print(fish_list)
    for fish in fish_list:

        fish_num, fish_dir = fish[0], fish[1]
        position = find_fish_location(board, fish_num)

        if position != None:
            row, col = position[0], position[1]

            # 순서대로 돌아가는거 만듬
            dir_list = [x for x in range(1, 9)]
            dir_list = [*dir_list[fish_dir - 1:], *dir_list[:fish_dir - 1]]

            for dir in dir_list:
                nrow, ncol = row + dirs[dir][0], col + dirs[dir][1]
                # print(nrow, ncol)

                if 0 <= nrow < 4 and 0 <= ncol < 4:
                    if nrow != shark_loc[0] and ncol != shark_loc[1]:
                        # 자리 바꿈
                        board[row][col], board[nrow][ncol] = board[nrow][ncol], board[row][col]
                        break
    return board


# 가능한 자리 찾기
def get_possible_positions(board, shark_loc):
    print("get_possible_positions")
    print("상어", shark_loc)
    pprint.pprint(board)
    position_list = []
    now_row, now_col = shark_loc[0], shark_loc[1]
    dir = board[now_row][now_col][1]

    for i in range(4):
        now_row += dirs[dir][0]
        now_col += dirs[dir][1]

        if 0 <= now_row and now_row < 4 and 0 <= now_col and now_col < 4:
            if board[now_row][now_col][0] != -1:

                position_list.append((now_row, now_col))

    return position_list


def dfs(board, shark_loc, total, fish_list):
    global answer
    global dirs

    board = copy.deepcopy(board)
    print("현재 상어 위치: ", shark_loc)
    pprint.pprint(board)


    row, col = shark_loc[0], shark_loc[1]
    if board[row][col][0] != -1:
        fish_num = board[row][col][0]
        board[row][col][0] = -1  # 물고기를 먹었으니까 -1로 표시
        # print(fish_num)
        total += fish_num

    # print(fish_list)
    for fish in fish_list:
        if fish[0] == fish_num:
             # 먹힌 물고기 점수 추가
            fish_list.remove(fish)  # 물고기 리스트에서 잡아먹힌 물고기 삭제

    # pprint.pprint(board)

    board = all_fish_move(board, fish_list, shark_loc)  # 물고기들 이동

    position_list = get_possible_positions(board, shark_loc)

    if len(position_list) == 0:
        answer = max(answer, total)
        return

    for position in position_list:
        # print("o", position, total)
        dfs(board, position, total, fish_list)


for tc in range(1, T + 1):
    board = []
    fish_list = []
    answer = 0

    for i in range(4):
        line = []
        fish_input = list(map(int, input().split()))
        for j in range(4):
            fish = [fish_input[2 * j], fish_input[(2 * j) + 1]]
            line.append(fish)
            fish_list.append(fish)
        board.append(line)
    # pprint.pprint(board)
    fish_list = sorted(fish_list, key=lambda x: x[0])
    shark_loc = (0, 0)  # 상어 현재 위치

    dfs(board, shark_loc, answer, fish_list)

    print("#{} {}".format(tc, answer))


    # print(sorted_fish_list)
    # print(shark_dir)
    # pprint.pprint(board)
    # board = all_fish_move(board)
    # pprint.pprint(board)



