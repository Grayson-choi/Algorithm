import sys

sys.stdin = open('input.txt', "r")

T = int(input())
for t in range(T):

    tunnel = {  # 왼 오 상 하 순으로 나열 / 각각 붙을 수 있는 터널의 번호를 딕셔너리의 요소로서 받음
        1: [[1, 3, 4, 5], [1, 3, 6, 7], [1, 2, 5, 6], [1, 2, 4, 7]],
        2: [[], [], [1, 2, 5, 6], [1, 2, 4, 7]],
        3: [[1, 3, 4, 5], [1, 3, 6, 7], [], []],
        4: [[], [1, 3, 6, 7], [1, 2, 5, 6], []],
        5: [[], [1, 3, 6, 7], [], [1, 2, 4, 7]],
        6: [[1, 3, 4, 5], [], [], [1, 2, 4, 7]],
        7: [[1, 3, 4, 5], [], [1, 2, 5, 6], []]
    }

    N, M, R, C, L = map(int, input().split())  # N:세로길이 M:가로길이 R: 맨홀위치 행 C: 맨홀위치 열 L: 소요시간
    mapp = []
    for _ in range(N):
        mapp.append(list(map(int, input().split())))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    time = 1
    cnt = 1

    qq = [(R, C)]
    while 1:
        if time == L:  # 소요시간이 되었다면 break
            break
        for _ in range(len(qq)):  # queue에 존재하는 요소를 모두 탐색해야 한 타임이 끝남!
            q = qq.pop(0)
            for i in range(4):
                if tunnel[mapp[q[0]][q[1]]][i]:  # (상 하 좌 우) 중 갈 수 있는 곳이 있다면
                    if 0 <= q[0] + dx[i] < N and 0 <= q[1] + dy[i] < M and mapp[q[0] + dx[i]][
                        q[1] + dy[i]] != 0:  # 벽이 아니고 터널이 존재한다면
                        if mapp[q[0] + dx[i]][q[1] + dy[i]] in tunnel[mapp[q[0]][q[1]]][i]:  # 그 터널이 갈 수 있는 터널이라면
                            if (q[0] + dx[i], q[1] + dy[i]) not in qq:  # queue에 중복요소 들어옴 방지
                                qq.append((q[0] + dx[i], q[1] + dy[i]))
                                cnt += 1
            mapp[q[0]][q[1]] = 0  # 상하좌우 체크가 끝나면 0으로 방문 처리함으로써 벽으로 만들어줌

        time += 1

    print('#{} {}'.format(t + 1, cnt))

# 12:00:25 실행이 완료되었습니다. 실행 시간 : 0.14364s
# 62,880 kb 메모리
# 255 ms 실행시간
