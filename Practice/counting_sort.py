from collections import Counter
nums = [0, 4, 1, 3, 1, 2, 4, 1]


def counting_sort(nums):
    answer_list = []
    print()
    for i in sorted(Counter(nums).items()):
        value, counter = i
        answer_list.append(counter)
    return answer_list


print(counting_sort(nums))