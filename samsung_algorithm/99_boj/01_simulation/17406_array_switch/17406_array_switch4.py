import sys
from collections import deque
from itertools import permutations
import copy

def rotate(y, x, height, width):
    global copy_arr
    q = deque()

    # 가로 줄 돌기
    for i in range(x, x + width):
        q.append(copy_arr[y][i])

    # 오른쪽 돌기
    for i in range(y + 1, y + height):
        q.append(copy_arr[i][x + width - 1])
        # print(i, x + width - 1)
        # print("--")


    for i in range(x + width - 2, x, -1):
        q.append(copy_arr[y + height - 1][i])
        print(y + height - 1, i)



    for i in range(y + height - 1, y, -1):
        q.append(copy_arr[i][x])

    q.rotate(1)  # 한칸 이동

    for i in range(x, x + width):
        copy_arr[y][i] = q.popleft()

    for i in range(y + 1, y + height):
        copy_arr[i][x + width - 1] = q.popleft()

    for i in range(x + width - 2, x, -1):
        copy_arr[y + height - 1][i] = q.popleft()

    for i in range(y + height - 1, y, -1):
        copy_arr[i][x] = q.popleft()


n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
op_infos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]
INF = int(1e9)  # 무한대로 설정
answer = INF
# print(op_infos)




op_orders = tuple(permutations(op_infos))
# print(op_orders)

for order in op_orders:
    copy_arr = copy.deepcopy(arr)
    for r, c, s in order:
        left_top_y = r - s - 1
        left_top_x = c - s - 1

        height = 2 * s + 1
        width = 2 * s + 1

        while True:
            if height <= 0 or width <= 0: break
            rotate(left_top_y, left_top_x, height, width)
            height -= 2
            width -= 2
            left_top_y += 1
            left_top_x += 1

    arr_value = INF
    for i in range(n):
        arr_value = min(arr_value, sum(copy_arr[i]))
    answer = min(answer, arr_value)

print(answer)