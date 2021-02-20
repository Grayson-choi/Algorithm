from pprint import pprint
"""
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.


그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)



[출력]


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
입력
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

출력
#1 4
#2 5
#3 7
"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    square_num = int(input())
    array = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(square_num):
        sq_input = list(map(int, input().split()))
        sq_x1, sq_y1, sq_x2, sq_y2, color  = sq_input[0], sq_input[1], sq_input[2], sq_input[3], sq_input[4]

        # 색칠하기
        for x in range(sq_x1, sq_x2 + 1):
            for y in range(sq_y1, sq_y2 + 1):
                if array[x][y] != color:
                    array[x][y] += color
                if array[x][y] == 3:
                    cnt += 1
    print("#{} {}".format(test_case, cnt))