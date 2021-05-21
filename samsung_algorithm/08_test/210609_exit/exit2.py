import sys
#
#
sys.stdin = open('input.txt', "r")


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    E = []  # 탈출구
    dis = [[], []]  # 비상구는 무조건 2개니까
    for i in range(n):
        for j in range(n):
            if factory[i][j] == 2:
                E.append([i, j])
    # print(E)
    for i in range(n):
        for j in range(n):
            if factory[i][j] == 1:
                dis[0].append(abs(i - E[0][0]) + abs(j - E[0][1]))
                dis[1].append(abs(i - E[1][0]) + abs(j - E[1][1]))
    print(dis)
    N = len(dis[0])  # 사람 수 길이만큼 만듬

    visit = [False] * N
    result = []
    # print(dis)
    while True:
        diff = []
        for i in range(N):
            if not visit[i]:
                diff.append(dis[0][i]-dis[1][i])  # 가까운 것을 찾기 위해서 1번 탈출구와 2번 탈출구 간의 거리를 확인
        a, b = min(diff), max(diff)

        idx = 0
        if a >= 0 and b >= 0:
            idx = 1
        min_val = 987654321
        for i in range(N):
            if min_val > dis[idx][i] and not visit[i]:
                min_val = dis[idx][i]
        print("d", dis)

        tmp = []
        for i in range(N):
            if dis[idx][i] == min_val and not visit[i]:
                tmp.append([dis[(idx + 1) % 2][i] - dis[idx][i], i])
        print(tmp)
        print(visit)
        tmp.sort(reverse=True)
        if tmp[0][0] >= 0:
            visit[tmp[0][1]] = True
            for i in range(N):
                if dis[idx][i] == min_val:
                    dis[idx][i] += 1 
                    # 같은 시간에 도착하면 +1 초
        result.append(min_val+1)  # 타는데 1초 걸림
        if visit.count(False) == 0:  # 모두 방문하면 종료
            break
    print('#{} {}' .format(tc, max(result)))