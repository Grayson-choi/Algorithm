""""
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

출력
#1 731
#2 18641
#3 2412
"""

T = int(input())
for test_case in range(1, T + 1):
    n, target = map(int, input().split())
    nums = list(input().split())
    for _ in range(target):
        tmp = nums.pop(0)
        nums.append(tmp)
    print("#{} {}".format(test_case, nums[0]))
