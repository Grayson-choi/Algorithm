import sys
import itertools

"""
15
12 34 17 6 11 15 27 42 39 31 25 36 35 25 17

17984
"""

# sys.stdin = open("input.txt", "rt")



num = int(input())
num_list = input().split()
result = []
def reverse(num):
    return int(num[::-1])

def is_prime(num):
    if num == 1:
        return False

    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True

for i in num_list:
    if is_prime(reverse(i)):
        result.append(str(reverse(i)))



# print("#{} {}".format(test_case, result))