import sys

# sys.stdin = open("input.txt", "rt")
T = int(input())

for test_case in range(1, T + 1):
    num, start, end, target = map(int, input().split())
    num_list = list(map(int, input().split()))
    result = sorted(num_list[start - 1:end])[target - 1]
    print("#{} {}".format(test_case, result))