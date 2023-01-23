import sys
import itertools

# sys.stdin = open("input.txt", "rt")

num_list = list(map(int, input().split()))
num1, num2 = num_list[0], num_list[1]
result = []
if num1 == num2:
    result.append(num1 + 1)
else:
    larger = max(num1, num2)
    smaller = min(num1, num2)
    for i in range(smaller + 1, smaller + (larger - smaller) + 2):
        result.append(i)
# print(result)
# 출력 하는 코드
result = list(map(str, result))
print(" ".join(result))






# print("#{} {}".format(test_case, result))