def move(position):
    r, c = position[0], position[1]
    v_num = state[position][0][0]
    d = state[position][0][1]
    if d == 1:
        if r - 1 == 0:
            v_num //= 2
            d = 2

        if (r - 1, c) not in state_next:
            state_next[(r - 1, c)] = [[v_num, d]]
        else:
            state_next[(r - 1, c)].append([v_num, d])

    elif d == 2:
        if r + 1 == N - 1:
            v_num //= 2
            d = 1

        if (r + 1, c) not in state_next:
            state_next[(r + 1, c)] = [[v_num, d]]
        else:
            state_next[(r + 1, c)].append([v_num, d])

    elif d == 3:
        if c - 1 == 0:
            v_num //= 2
            d = 4

        if (r, c - 1) not in state_next:
            state_next[(r, c - 1)] = [[v_num, d]]
        else:
            state_next[(r, c - 1)].append([v_num, d])

    elif d == 4:
        if c + 1 == N - 1:
            v_num //= 2
            d = 3

        if (r, c + 1) not in state_next:
            state_next[(r, c + 1)] = [[v_num, d]]
        else:
            state_next[(r, c + 1)].append([v_num, d])


def merge(position):
    L = len(state_next[po])
    if L > 1:
        s = 0
        tmp_vnum = 0
        Clusters = state_next[po]
        for i in range(L):
            s += Clusters[i][0]
            if tmp_vnum < Clusters[i][0]:
                tmp_vnum = Clusters[i][0]
                d = Clusters[i][1]
        state_next[po] = [[s, d]]


T = int(input())
for test in range(T):
    N, M, K = map(int, input().split())  # 배열크기, 몇시간뒤? , 군집수
    state = {}
    for i in range(K):
        r, c, virus_num, d = map(int, input().split())
        state[(r, c)] = [[virus_num, d]]  # d: 1 2 3 4 / 상 하 좌 우
    for time in range(M):

        state_next = {}
        for po in state:
            move(po)

        for po in state_next:
            merge(po)

        state = state_next

    sol = 0
    for key in state:
        sol += state[key][0][0]
    print('#%d' % (test + 1), sol)

# 13:44:52 실행이 완료되었습니다. 실행 시간 : 0.17602s
# 66,320 kb 메모리
# 559 ms 실행시간