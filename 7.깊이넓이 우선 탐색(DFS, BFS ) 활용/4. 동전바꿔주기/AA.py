import sys

"""
19
4
4 4
5 3
2 3
7 3
"""

# sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(coin_n[L] + 1):
            DFS(L + 1, sum + (coin_v[L] * i))

T = int(input())
k = int(input())
coin_v = list()
coin_n = list()
for i in range(k):
    a, b = map(int, input().split())
    coin_v.append(a)
    coin_n.append(b)
cnt = 0
DFS(0, 0)
print(cnt)

