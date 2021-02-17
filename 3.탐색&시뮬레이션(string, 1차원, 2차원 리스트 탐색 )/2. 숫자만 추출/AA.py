import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
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

word = input()
nums = []
for char in word:
    if char.isdigit():
        nums.append(char)

for i in range(len(nums)):
    if nums[0] == "0":
        nums.pop(0)

num = "".join(nums)
print(num)

cnt = 0
num = int(num)
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1
print(cnt)