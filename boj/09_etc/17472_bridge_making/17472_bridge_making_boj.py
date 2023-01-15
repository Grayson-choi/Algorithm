import queue

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(board, start, cnt):
    global visited
    global m_row, m_col
    global dx
    global dy

    q = queue.Queue()
    q.put(start)
    x, y = start

    while not q.empty():
        x, y = q.get()
        board[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m_row or ny >= m_col:
                continue  # 범위 제한 체크

            if board[nx][ny] == 0 or board[nx][ny] > 1:
                continue  # 벽 체크

            board[nx][ny] = cnt
            q.put((nx, ny))


# 간선의 정보를 가져온다.
def find_path(x, y, island_num):
    global dx
    global dy
    global distances
    global m_row, m_col
    global cost
    global dis_dict

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        distance = 0
        # print("현재 위치", x, y, island_num)

        while True:
            # 밖으로 벗어나면 취소
            # print("다음 위치", nx, ny)
            if nx < 0 or ny < 0 or nx >= m_row or ny >= m_col:
                # print("범위 벗어남")
                break
            # 자기자신과 만나면 취소
            if board[nx][ny] == island_num:
                # print("같은 섬임")
                break
            # 진행방향이 바다라면 한번더 진행하고 거리 count
            if board[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                distance += 1
                # print("바다니까 한번 더 진행중", nx, ny, "d", distance)
                continue
            if board[nx][ny] != island_num:

                # print("b", board[nx][ny], "start", island_num)
                # print(f"출발점: {island_num} 다른 섬 만남 {board[nx][ny]} 거리는: ", distance)

                if distance < 2:         # 길이가 2 이하라면 취소
                    break

                # 거리 추가하기
                target = board[nx][ny]
                cost = distances[island_num - 2][target - 2]

                # 0이면 연결된 적이 없음
                if cost == 0:
                    # print(distance)
                    distances[island_num - 2][target - 2] = distance
                    # print("c", count)
                    dis_dict[(island_num,target)] = distance
                    # print("연결")
                    # print(dis_dict)
                else:
                    minimum_distance = min(cost, distance)
                    # print(minimum_distance)
                    distances[island_num - 2][target - 2] = min([cost, distance])
                    dis_dict[(island_num, target)] = min(cost, distance)
                    # dis_dict[(target, island_num)] = min(cost, distance)
                    # print(dis_dict)
                break






m_row, m_col = list(map(int, input().split()))
# print(m_row, m_col)

board = []
cost = []
answer = 0
for _ in range(m_row):
    board.append(list(map(int, input().split())))


cnt = 2

# 섬번호 붙이기
for row in range(m_row):
    for col in range(m_col):
        if board[row][col] == 1:
            # print("섬", row, col)
            bfs(board, (row, col), cnt)
            cnt += 1
# pprint.pprint(board)

costs = []

# 각 이동 거리에 대한 배열
distances = [[0 for j in range(cnt)] for i in range(cnt)]
dis_dict = {}
# 섬과 연결하기
for row in range(m_row):
    for col in range(m_col):
        count = board[row][col]
        if count > 0:
            find_path(row, col, count)
# pprint.pprint(distances)

# 최소 거리 계산하기
visited = [0] * (cnt + 1)

# print(dis_dict)
sorted_tuples = sorted(dis_dict.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}
# print(sorted_dict)  # 모든 다리가 저장되어 있음
# print(dis_dict)
parent = [i for i in range(cnt - 2)]


def make_set(x):
    parent[x] = x

for i in range(cnt - 2):
    make_set(i)
# print(parent)

# 부모의 정보를 가져온다.
def getParent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = getParent(parent[idx])
    return parent[idx]

# 부모를 병합한다. 작은 부모에게 병합
def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모가 같은지 확인한다.
def find(a, b):
    a = getParent(a)
    b = getParent(b)
    return a == b


for path in sorted_dict:
    # print(path, sorted_dict[path])
    start, end = path
    start -= 2
    end -= 2
    # print(start, end)
    distance = sorted_dict[path]
    if not find(start, end):
        answer += distance
        # print("answer", answer)
        unionParent(start, end)
        # print(parent)

# 모든섬이 연결되었나 확인한다.
for i in range(cnt - 2):
    # 하나라도 연결이 되어있지 않다면 -1로 바꾼다
    if getParent(i) != 0:
        answer = -1
        break

print(answer)


