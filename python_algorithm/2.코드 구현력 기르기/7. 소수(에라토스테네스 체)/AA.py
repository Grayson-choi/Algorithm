import sys
import itertools

num = int(input())
check_list = [0] * (num + 1)
cnt = 0

for i in range(2, num + 1):
    if check_list[i] == 0:
        cnt += 1
        for j in range(i, num + 1, i):
            check_list[j] = 1

print(cnt)
