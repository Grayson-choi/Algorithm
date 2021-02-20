T = int(input())

for test_case in range(1, T + 1):

for t in range(int(input())):
    k, n, m = map(int, input().split())
    #: k 이동거리 n: 종점 m: 충전기 설치된 개수
    number = list(map(int, input().split()))
    print(number)
    charge = [0] * (n + 1)  # 충전기 설치
    visited = [0] * (n + 1)
    print(visited)
    for i in number:
        charge[i] = 1
    print(charge)
    dis = k
    now = k
    while True:
        if now >= n:
            result = sum(visited)
            break
        elif charge[now] == 1:
            dis = k
            visited[now] = 1
            now += k
        elif charge[now] == 0:
            now -= 1
            dis -= 1
            if dis == 0:
                result = 0
                break

    print("#{} {}".format(t + 1, result))