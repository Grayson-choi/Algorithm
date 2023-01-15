#리스트를 반으로 나눈다.
# 왼쪽과 오른쪽을 정렬한다.

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

    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))