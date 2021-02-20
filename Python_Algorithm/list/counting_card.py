"""
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.




[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

3
5
49679
5
08271
10
7797946543


#1 9 2
#2 8 1
#3 7 3

"""
import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card_num = int(input())
    card_list = list(map(int, input()))
    cards = sorted(collections.Counter(card_list).items(), key=lambda kv: kv[1], reverse=True)
    num, count = cards[0]
    # 동점일 경우 처리
    filtered = [item for item in cards if item[1] == count]
    if len(filtered) > 1:
        num, count = max(filtered)

