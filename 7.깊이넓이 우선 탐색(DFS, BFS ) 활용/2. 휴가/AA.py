import sys

"""
5 20
10 5
25 12
15 8
6 3
7 4

"""

# sys.stdin = open("input.txt", "r")

def DFS(n, sum):
    global result
    if n == D + 1:
        if sum > result:
            result = sum
    else:
        if n + times[n] <= D + 1:
            DFS(n + times[n], sum + profits[n])
        DFS(n + 1, sum)

D = int(input())
times = []
profits = []

for _ in range(D):
    t, p = map(int, input().split())
    times.append(t)
    profits.append(p)

times.insert(0, 0)
profits.insert(0, 0)
result = -100000
DFS(1, 0)
print(result)
