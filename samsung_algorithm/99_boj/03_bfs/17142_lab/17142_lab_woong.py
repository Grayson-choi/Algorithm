import sys
import pprint
import queue
from itertools import combinations
import copy


sys.stdin = open('input.txt', "r")

T = int(input())

def bfs(v_list, visited):
    global board
    global place
    global result

    board = board[:]
    # print(v_list)
    q = queue.Queue()
    count = 0

    for start in v_list:
        x, y = start[0], start[1]
        q.put((x, y))
        visited[x][y] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # print(v_list, virus_list)
    # 비활성 바이러스 처리

    for x in range(len(board)):
        for y in range(len(board[0])):
            if visited[x][y] == 0 and (x, y) not in v_list and (x, y) in virus_list:
                visited[x][y] = "-"
    # pprint.pprint(visited)


    virus_done = 0

    while not q.empty():
        x, y = q.get()
        if visited[x][y] + 1 > result:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                continue  # 범위 제한 체크

            if visited[nx][ny] == "-":
                continue  # 벽 체크
            if visited[nx][ny] != 0:
                if visited[nx][ny]:
                    continue

            # pprint.pprint(visited)

            if visited[nx][ny] == 0: # 바이러스가 퍼질 수 있는 곳이면
                visited[nx][ny] = visited[x][y] + 1
                q.put((nx, ny))
                virus_done -= 1


    # pprint.pprint(visited)
    max_time = 0
    zero_count = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if visited[x][y] == "-":
                continue
            if visited[x][y] > max_time:
                max_time = visited[x][y]
            if visited[x][y] == 0 and board[x][y] != 2:
                zero_count += 1

    if zero_count != 0:
        return

    result = min(result, max_time)
    # print("max", max_time, "z", zero_count, "v_list", len(v_list), "r", result)




for tc in range(1, T + 1):
    row, virus_num = list(map(int, input().split()))
    board = []
    for _ in range(row):
        board.append(list(map(int, input().split())))
    # pprint.pprint(board)
    print(f"#{tc}")
    result = 10 ** 6

    visited = [[0] * len(board[0]) for _ in range(len(board))]

    place = 0

    # 벽 위치 처리 및 바이러스 위치 찾기
    virus_list = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 1:
                board[x][y] = "-"
                visited[x][y] = "-"
            if board[x][y] == 2:
                virus_list.append((x, y))
            if board[x][y] == 0:
                place += 1
    # print("p", place)
    # print("v", virus_list)

    virus_combination = list(combinations(virus_list, virus_num))
    # print(virus_combination)

    # print("바이러스전")
    # pprint.pprint(visited)

    # 바이러스 퍼지는거 만들기

    virus_cnt = 0
    for virus_case in virus_combination:
        virus = virus_case
        arr = copy.deepcopy(visited)
        bfs(virus, arr)
    # print("바이러스 후")
    # pprint.pprint(visited)
    # print("-" * 100)
    if result > 10 ** 5:
        print(-1)
    else:
        print(result)


