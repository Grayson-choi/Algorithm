import queue
from itertools import combinations
import copy


def bfs(v_list, visited):
    global place
    global result

    q = queue.Queue()
    count = 0
    place = 0

    for start in v_list:
        x, y = start[0], start[1]
        q.put((x, y, count))
        visited[x][y] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    virus_done = 0

    while not q.empty():
        x, y, cnt = q.get()

        if visited[x][y] + 1 < cnt:
            break

        if visited[x][y] > result:
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
                if visited[x][y] + 1 > result:
                    break
                q.put((nx, ny, cnt + 1))
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

row, virus_num = list(map(int, input().split()))
board = []
for _ in range(row):
    board.append(list(map(int, input().split())))
# pprint.pprint(board)
# print(f"#{tc}")
result = 10 ** 6

visited = [[0] * len(board[0]) for _ in range(len(board))]

place = 0

# 벽 위치 처리 및 바이러스 위치 찾기
virus_list = []
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == 1:
            visited[x][y] = "-"
        if board[x][y] == 2:
            virus_list.append((x, y))
# print("p", place)
# print("v", virus_list)

virus_combination = list(combinations(virus_list, virus_num))
# print(virus_combination)

# print("바이러스전")
# pprint.pprint(visited)

# pprint.pprint(visited)

# 바이러스 퍼지는거 만들기

virus_cnt = 0
for virus_case in virus_combination:
    virus = virus_case
    arr = copy.deepcopy(visited)
    for x in range(len(board)):
        for y in range(len(board[0])):
            if arr[x][y] == 0 and (x, y) not in virus_case and (x, y) in virus_list:
                arr[x][y] = "-"
    bfs(virus, arr)

    # 비활성 바이러스 처리



# print("바이러스 후")
# pprint.pprint(visited)
# print("-" * 100)
if result > 10 ** 5:
    print(-1)
else:
    print(result)


