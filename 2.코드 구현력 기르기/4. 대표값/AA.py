import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17
"""

# sys.stdin = open("input.txt", "rt")

num = int(input())
num_list = list(map(int, input().split()))
avg = int((sum(num_list) / num) + 0.5)
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