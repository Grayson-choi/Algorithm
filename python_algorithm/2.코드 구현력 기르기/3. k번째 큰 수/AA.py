import sys
import itertools

num, target = map(int, input().split())
num_list = list(map(int, input().split()))
nCr = itertools.combinations(num_list, 3)
res = set()

for i in range(num):
    for j in range(i + 1, num):
        for k in range(j + 1, num):
            res.add(num_list[i] + num_list[j] + num_list[k])

result = sorted(res, reverse=True)[target - 1]
print(result)
