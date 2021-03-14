import sys

"""
5
4 7 10 22 25
"""

# sys.stdin = open("input.txt", "r")

def DFS(n, num):
    global ck_list
    if n == N + 1:
        if 0 < num <= pos:
            ck_list.add(num)

    else:
        DFS(n + 1, num + weights[n])
        DFS(n + 1, num - weights[n])
        DFS(n + 1, num)

N = int(input())
weights = list(map(int, input().split()))
weights.insert(0, 0)
pos = sum(weights)
ck_list = set()
DFS(1, 0)
print(pos - len(ck_list))


