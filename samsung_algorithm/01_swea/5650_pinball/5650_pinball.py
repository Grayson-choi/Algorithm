# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 1~5 블럭 방향전환
change = (
    'dummy',
    # index : 입사방향 # value : 출사방향
    (1, 3, 0, 2),
    (3, 0, 1, 2),
    (2, 0, 3, 1),
    (1, 2, 3, 0),
    (1, 0, 3, 2)
)


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input()) + 2
    # 가장자리에 5번 블럭 더함
    MAP = [[5] * N] + [[5] + list(map(int, input().split())) + [5] for _ in range(N - 2)] + [[5] * N]

    # 웜홀
    # dummy 는 숫자 index를 편하게 맞추기 위한 공간
    worm_stack = ['dummy'] * 6 + [None] * 5
    wormhole = {}
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if MAP[r][c] in range(6, 11): # MAP[r][c] : 6~10(웜홀)
                worm_start = worm_stack[MAP[r][c]]
                if not worm_start: # 등록된 웜홀이 없으면
                    worm_stack[MAP[r][c]] = (r, c) # 시작 지점을 stack 에 저장.
                else: # 등록된 웜홀이 있으면 (출구)
                    wormhole[worm_start] = (r, c) # 웜홀 시작점의 끝을 출구값으로 저장
                    wormhole[(r, c)] = worm_start # 웜홈의 출구에 시작점을 저장.

    # 탐색
    result = 0
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if MAP[r][c] == 0: # 빈 공간(통로인 경우) : 핀볼의 시작점이 될 수 있다.
                for d in range(4):  # 상하좌우
                    cnt = 0
                    y, x = r + dy[d], c + dx[d]
                    while True:
                        # 시작지점이거나 블랙홀이면 종료
                        if (y, x) == (r, c) or MAP[y][x] == -1:
                            break

                        # 1 ~ 5 블럭에 와있으면 방향 전환, 득점
                        elif MAP[y][x] in range(1, 6):
                            d = change[MAP[y][x]][d]
                            cnt += 1

                        # 6 ~ 10 블럭에 와있으면 워프
                        elif MAP[y][x] in range(6, 11):
                            y, x = wormhole[(y, x)]

                        # 한 칸 전진
                        y, x = y + dy[d], x + dx[d]

                    # 탐색 종료되면 결과 갱신
                    if cnt > result:
                        result = cnt

    print('#{} {}'.format(test_case, result))