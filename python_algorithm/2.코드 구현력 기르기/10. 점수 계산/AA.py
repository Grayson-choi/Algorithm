import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
"""

# sys.stdin = open("input.txt", "rt")


n = int(input())
num_list = list(map(int, input().split()))
result = 0
cnt = 0
for i in num_list:
    if i == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0
print(result)




# print("#{} {}".format(test_case, result))