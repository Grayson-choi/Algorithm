"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
"""

T = int(input())

for test_case in range(1, T + 1):
    V, edge_num = list(map(int, input().split()))
    graph = {key:[] for key in range(1, V + 1)}
    visited = []
    for _ in range(edge_num):
        key, value = list(map(int, input().split()))
        graph[key].append(value)
    start, end = map(int, input().split())
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    if end in visited:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))


