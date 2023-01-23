import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17
"""

# sys.stdin = open("input.txt", "rt")


num = int(input())
num_list = list(map(int, input().split()))
sum_list = []

def digit_sum(num):
    return sum([int(x) for x in num])

for i in num_list:
    sum_list.append(digit_sum(str(i)))

index = sum_list.index(max(sum_list))
print(num_list[index])






# print("#{} {}".format(test_case, result))