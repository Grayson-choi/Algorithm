import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17
"""

sys.stdin = open("input.txt", "rt")
# T = int(input())
#
# for test_case in range(1, T + 1):

# num, target = map(int, input().split())
# num_list = list(map(int, input().split()))
# nCr = itertools.combinations(num_list, 3)
# nCr_set = set(map(sum, nCr))
# print(sorted(nCr_set, reverse=True)[target - 1])


import math

num = int(input())
num_list = list(map(int, input().split()))
avg = round(sum(num_list) / num)
num_list.append(avg)
sorted_list = sorted(num_list)
avg_index = sorted_list.index(avg)
front = abs(sorted_list[avg_index - 1] - sorted_list[avg_index])
back = abs(sorted_list[avg_index + 1] - sorted_list[avg_index])

if front < back:
    result = sorted_list[avg_index - 1]
    result_index = num_list.index(result) + 1
    print(avg, result_index, sep=" ")
else:
    result = sorted_list[avg_index + 1]
    result_index = num_list.index(result) + 1
    print(avg, result_index, sep=" ")




# print("#{} {}".format(test_case, result))