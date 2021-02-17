import sys
import itertools

"""
10
1 10 27 39 50 61 65 70 93 93 
7
7 51 65 66 70 82 93 
"""
#
# sys.stdin = open("input.txt", "rt")
#
#
# n = int(input())
#
# for test_case in range(1, n + 1):
#     word = input()
#     if word == word[::-1]:
#         print("#{} YES".format(test_case))
#     else:
#         print("#{} NO".format(test_case))
nums = [x for x in range(1, 20 + 1)]
list1_len = int(input())
list1 = list(map(int, input().split()))
list2_len = int(input())
list2 = list(map(int, input().split()))

result = list(map(str, sorted([*list1, *list2])))

print(" ".join(result))

# for _ in range(10):
#     start, end = map(int, input().split())
#     start_list = nums[:start - 1]
#     middle_list = list(reversed(nums[start - 1:end]))
#     end_list = nums[end:]
#     nums = [*start_list, *middle_list, *end_list]
#
# print(" ".join(list(map(str, nums))))