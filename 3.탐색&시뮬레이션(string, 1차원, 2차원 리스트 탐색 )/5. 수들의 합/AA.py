import sys
import itertools

"""
10
1 10 27 39 50 61 65 70 93 93 
7
7 51 65 66 70 82 93 
"""
#
# sys.stdin = open("input.txt", "rt")


list_len, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
left, right = 0, 1
cnt = 0
total = nums[0]

while True:
    if total < target:
        if right < list_len:
            total += nums[right]
            right += 1
        else:
            break
    elif total == target:
        cnt += 1
        total -= nums[left]
        left += 1
    else:
        total -= nums[left]
        left += 1

print(cnt)


# for _ in range(10):
#     start, end = map(int, input().split())
#     start_list = nums[:start - 1]
#     middle_list = list(reversed(nums[start - 1:end]))
#     end_list = nums[end:]
#     nums = [*start_list, *middle_list, *end_list]
#
# print(" ".join(list(map(str, nums))))