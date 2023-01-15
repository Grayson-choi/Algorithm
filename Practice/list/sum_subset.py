from pprint import pprint
"""
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

입력
3
3 6
5 15
5 10

출력
#1 1
#2 1
#3 0
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, target = list(map(int, input().split()))
    arr = [x + 1 for x in range(12)]
    lst = []
    # 부분 집합 구하기
    for i in range(1 << 12):  # 1<<n: 부분 집합의 개수
        subsets = []
        for j in range(12):
            if i & (1 << j):  # i에서 j번째 비트가 1인지 아닌지를 리턴함
                subsets.append(arr[j])
        if len(subsets) == n:
            lst.append(subsets)
    result = len([x for x in lst if sum(x) == target])
    print("#{} {}".format(test_case, result))

# https://itzjamie96.github.io/2020/10/15/python-bitwise-powersets/