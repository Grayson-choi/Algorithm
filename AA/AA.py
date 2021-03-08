import sys

"""
5 20
10 5
25 12
15 8
6 3
7 4

"""

sys.stdin = open("input.txt", "r")


def dfs(v):
    if v > n:
        sub_sums = []
        for i in range(n):
            if ck_list[i] == 1:
                sub_sums.append(nums[i])
        sub_sum = sum(sub_sums)
        print(sub_sum)
    print()

    ck_list[v] = 1
    dfs(v + 1)
    ck_list[v] = 0
    dfs(v + 1)


if __name__ == "__main__":
    n, time = map(int, input().split())
    p_score = [0] * (n + 1)
    p_time = [0] * (n + 1)

    for i in range(n):
        score, time = map(int, input().split())
        
    nums = list(map(int, input().split()))
    ck_list = [0] * (n + 1)
    sums = []
    dfs(1)
