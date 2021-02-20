# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.


N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
입력
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
출력
#1 630739
#2 740510
#3 838110
"""
T = int(input())
for test_case in range(1, T + 1):
    num_count = int(input())
    nums = list(map(int, input().split()))
    result = max(nums) - min(nums)
    print("#{} {}".format(test_case, result))
