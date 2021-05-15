import sys
import pprint
import queue
sys.stdin = open('input.txt', "r")

T = int(input())


for tc in range(1, T + 1):
    row, col = list(map(int, input().split()))
    maze = []
    for _ in range(row):
        maze.append(list(map(int, list(input()))))
    # print(row, col)
    pprint.pprint(maze)
    q = queue.Queue()
    visited = [[0] * col for x in range(row)]
    # pprint.pprint(visited)
    start, end = (0, 0)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.put((start, end))
    visited[start][end] = 1
    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue  # 범위 제한 체크

            if maze[nx][ny] == 0:
                continue  # 벽 체크

            if visited[nx][ny] != 0:
                continue  # 방문했는지 체크
            else:
                q.put((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            # print(visited)

    print(visited[row - 1][col - 1])


