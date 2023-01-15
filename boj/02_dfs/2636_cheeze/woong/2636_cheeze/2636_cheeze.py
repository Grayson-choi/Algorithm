import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")
# sys.setrecursionlimit(5000) # 5000
print(sys.getrecursionlimit())  # 1000

def count_empty(x, y):
    global table
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if visited[x][y] == 1:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            continue
        if table[nx][ny] == 0 or table[nx][ny] == 3:
            visited[x][y] = 1
            table[x][y] = 3
            count_empty(nx, ny)


def check_edge(x, y):
    global table
    global edge

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            return
        if table[x][y] == 1 and table[nx][ny] == 3:
            return True


row, col = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
cheeze = 0
edge = 0
cnt = 0
# 치즈 갯수 count
for x in range(row):
    for y in range(col):
        if table[x][y] == 1:
            cheeze += 1

while cheeze > 0:
    visited = [[0] * col for _ in range(row)]
    edge = 0
    count_empty(0, 0)
    for x in range(row):
        for y in range(col):
            if check_edge(x, y):
                table[x][y] = 0
                visited[x][y] = 1
                edge += 1
    cnt += 1
    cheeze -= edge
    pprint(table)
    print("-----")
    pprint(visited)

print(cnt)
print(edge)
