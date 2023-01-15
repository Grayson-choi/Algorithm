def merge(list1, list2):
    # 코드를 작성하세요.
    index_a = 0
    index_b = 0
    list = []

    while index_a < len(list1) and index_b < len(list2):
        if list1[index_a] > list2[index_b]:
            list.append(list2[index_b])
            index_b += 1
        else:
            list.append(list1[index_a])
            index_a += 1

    if index_a == len(list1):
        list += list2[index_b:]
    
    if index_b == len(list2):
        list += list1[index_a:]

    return list

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list

    index = len(my_list) // 2
    list1 = my_list[:index]
    list2 = my_list[index:]
    
    return merge(merge_sort(list1),merge_sort(list2))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
