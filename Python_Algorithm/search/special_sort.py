"""
입력
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21

"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num_list = sorted(map(int, input().split()), reverse=True)
    cnt = 0
    idx = 0
    m_idx = -1
    reversed_list = []
    for i in range(10):
        if cnt % 2 == 0:
            reversed_list.append(num_list[idx])
            idx += 1
        else:
            reversed_list.append(num_list[m_idx])
            m_idx -= 1
        cnt += 1
    result = " ".join(map(str, reversed_list))


    print("#{} {}".format(test_case, result))