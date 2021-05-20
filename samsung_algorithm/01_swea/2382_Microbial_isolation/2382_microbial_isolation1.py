# 무 상 하 좌 우
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
rev = [0, 2, 1, 4, 3]  # 방향 전환

T = int(input())
for test_case in range(1, 1 + T):
    N, M, K = map(int, input().split())
    my_map = [[None] * N for _ in range(N)]
    m_list = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        check = {}
        idx = -1
        for m in m_list:
            y, x, cnt, d = m
            idx += 1
            if not cnt:
                continue  # 다음 미생물

            # 이동
            ny, nx = y + dy[d], x + dx[d]
            m[0], m[1] = ny, nx
            # 약품으로 이동 시 반감 후 방향 전환
            if ny == 0 or ny == N - 1 or nx == 0 or nx == N - 1:
                m[2] //= 2
                m[3] = rev[m[3]]

            # 중복 체크
            if (ny, nx) not in check:  # 좌표에 아무도 없으면
                check[(ny, nx)] = (idx, cnt)  # 최대 미생물 등록
            else:  # 좌표에 있으면(겹침)
                max_idx, max_cnt = check[(ny, nx)]  # 최대 미생물
                if max_cnt < cnt:  # 보다 크면
                    check[(ny, nx)] = (idx, cnt)  # 등록
                    m[2] += m_list[max_idx][2]  # 흡수
                    m_list[max_idx][2] = 0
                else:  # 작으면
                    m_list[max_idx][2] += m[2]  # 흡수 당함
                    m[2] = 0

    # 결과
    result = sum(map(lambda x: x[2], m_list))
    print('#{} {}'.format(test_case, result))

# 13:44:19 실행이 완료되었습니다. 실행 시간 : 0.18102s
# 69,484 kb 메모리
# 705 ms 실행시간
