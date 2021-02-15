import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
"""

# sys.stdin = open("input.txt", "rt")


n = int(input())
result = []
for i in range(n):
    num_list = list(map(int, input().split()))
    if num_list[0] == num_list[1] == num_list[2]:
        result.append(10000 + num_list[0] * 1000)
    elif num_list[0] == num_list[1] or num_list[1] == num_list[2]:
        result.append(1000 + num_list[1] * 100)
    elif num_list[0] == num_list[2]:
        result.append(1000 + num_list[2] * 100)
    else:
        result.append(100 + max(num_list) * 100)

print(max(result))




# print("#{} {}".format(test_case, result))