import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    table = []
    for _ in range(4):
        line = list(map(int, input().split()))
        for i in range(4):
            fish_num = line[i]
            dir = line[i + 1]

