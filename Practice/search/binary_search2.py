"""
입력
3
400 300 350
1000 299 578
1000 222 888

출력
#1 A
#2 0
#3 A
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    page, a_target, b_target = map(int, input().split())
    a_start = 1
    a_end = page
    a_middle = int((a_start + a_end) / 2)

    b_start = 1
    b_end = page
    b_middle = int((b_start + b_end) / 2)

    a_cnt, b_cnt = 0, 0
    winner = 0

    while a_target != a_middle:
        if a_target > a_middle:
            a_start = a_middle
            a_cnt += 1
        elif a_target < a_middle:
            a_end = a_middle
            a_cnt += 1
        a_middle = int((a_start + a_end) / 2)

    while b_target != b_middle:
        if b_target > b_middle:
            b_start = b_middle
            b_cnt += 1
        elif b_target < b_middle:
            b_end = b_middle
            b_cnt += 1
        b_middle = int((b_start + b_end) / 2)

    if a_cnt < b_cnt:
        winner = "A"
    elif a_cnt > b_cnt:
        winner = "B"
    print("#{} {}".format(test_case, winner))



