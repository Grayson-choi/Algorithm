def binary_search(element, some_list, start_index=0, end_index=None):

    if end_index == None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return None
    # 범위의 중간 인덱스를 찾는다
    mid_index = (start_index + end_index) // 2

    # 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid_index] == element:
        return mid_index

    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid_index]:
        return binary_search(element, some_list, start_index, mid_index - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid_index + 1, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
