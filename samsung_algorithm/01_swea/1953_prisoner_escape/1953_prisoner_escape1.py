from collections import deque

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}

t = int(input())
for test in range(1,t+1):
    n, m, r, c, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    q = deque([(r, c)])
    visited[r][c] = 1
    cnt = 1

    while q:
        a, b = q.popleft()
        for dx, dy in tunnel[maps[a][b]]:
            nx = dx+a
            ny = dy+b
            if not 0<=nx<n or not 0<=ny<m :
                continue
            if (-dx, -dy) in tunnel[maps[nx][ny]]:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[a][b] + 1
                    q += [(nx, ny)]
                    if visited[nx][ny] <=l :
                        cnt += 1

    print('#{} {}'.format(test, cnt))

# 11:59:49 실행이 완료되었습니다. 실행 시간 : 0.21627s
# 64,440 kb 메모리
# 308 ms 실행시간