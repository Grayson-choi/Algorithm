nums = [1, 4, 3, 2]

def array_pair_sum(nums):
    sorted_list = sorted(nums)[::2]
    return sum(sorted_list)

print(array_pair_sum(nums))