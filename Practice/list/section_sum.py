"""
입력
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

출력
#1 21
#2 11088
#3 1090

"""

import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count_num, section = map(int, input().split())
    nums = list(map(int, input().split()))
    min_num = 1000000
    max_num = -10
    for i in range(count_num - section + 1):
        sum_result = sum(nums[i:i+section])
        if sum_result >= max_num:
            max_num = sum_result
        if sum_result <= min_num:
            min_num = sum_result
    result = max_num - min_num
    print("#{} {}".format(test_case, result))
