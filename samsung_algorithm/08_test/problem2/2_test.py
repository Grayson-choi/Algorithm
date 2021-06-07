import pprint
import queue
from collections import deque
import copy
import sys


sys.stdin = open('input.txt', "r")

T = int(input())


for tc in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input().split()))
    target = [x for x in range(1, n + 1)]
    target_desc = [y for y in range(n, 0, -1)]
    # print(target_desc)
    print(f"#{tc}, {n}")
    # print(arr)
    # arr = [list(map(int, input().split())) for _ in range(n)]

    # 반 나누기
    cnt = n // 2
    #
    # list_a = arr[0:cnt]
    # list_b = arr[cnt: n + 1]

    # print("x=0")


    # print(list_a, list_b)
    for x in range(n):
        if x == 0:
            list_a = arr[0:cnt]
            list_b = arr[cnt: n + 1]
            result = [*list_a, *list_b]
        else:
            list_a = result[0:cnt]
            list_b = result[cnt: n + 1]
            print("a", list_a, list_b)

        if x == 1:  # x가 1일 때
            result = []
            for i in range(cnt - x):
                result.append(list_a.pop(0))
            # print(result, list_a, list_b)
            result.append(list_b.pop(0))
            result.append(list_a.pop(0))
            for i in range(cnt - x):
                result.append(list_b.pop(0))
            # print("x=1", result)
        elif x == 2:
            for i in range(x):
                print("i", i)
                print(2 * i + x, (2 * i) + x - 1)
                result[2 * i + x], result[(2 * i) + x - 1] = result[(2 * i) + x - 1], result[2 * i + x]
            print("x=2", result)

        elif x == 3:
            # for i in range(x):
            #     result[2 * i + x], result[(2 * i) + x - 1] = result[(2 * i) + x - 1], result[2 * i + x]
            # print("x=2", result)
            pass


        # elif x == 4:
            # result = []
            # result = [*list_b, *list_a]
            # tmp = result[cnt]
            # result[cnt] = result[cnt - 1]
            # result[cnt - 1] = tmp
            # print("x=4", result)
        # elif x == 5:
        #     pass

        #
        # if result == target or result == target_desc:
        #     print("처리 후 결과",result)
        #     print("정렬 완료, {}번째".format(x))
        #     answer = x
        #     break
        #
        # if x > 6:
        #     answer = -1
        #     break

    # print("#{} {}".format(tc, answer))
    # print(result)