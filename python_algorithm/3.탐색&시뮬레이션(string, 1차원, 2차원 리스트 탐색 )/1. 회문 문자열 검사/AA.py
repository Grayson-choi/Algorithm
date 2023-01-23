import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
"""

# sys.stdin = open("input.txt", "rt")


n = int(input())

for test_case in range(1, n + 1):
    word = input().lower()
    if word == word[::-1]:
        print("#{} YES".format(test_case))
    else:
        print("#{} NO".format(test_case))


