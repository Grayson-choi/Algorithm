def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    result = 0
    for a in left_cards:
        for b in right_cards:
            if a * b > result:
                result = a * b
    return result
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))