import sys
import pprint
import queue
sys.stdin = open('test_input.txt', "r", encoding="utf-8")

# import timeit
# start = timeit.default_timer()

T = int(input())

d = [(0.5, 0), (-0.5, 0), (0, -0.5), (0, 0.5)]


# 0.5 만큼 움직인다.
def move(i):
    dy, dx = d[i[2]]
    return [i[0] + dx, i[1] + dy, i[2], i[3]]

# dic에 i를 병합.
def merge_dicts(i):
    x, y = i[0], i[1]
    try:
        dic[(x, y)].append(i)
    except:
        dic[(x, y)] = [i]


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    energy = 0
    for _ in range(4000):
        if len(arr) < 2:
            break
        dic = {}
        arr = list(map(move, arr))
        list(map(merge_dicts, arr))
        arr = []
        for i in dic:
            if len(dic[i]) > 1:
                item = dic[i]
                for en in item:
                    energy += en[3]
            else:
                item = dic[i]
                x = item[0][0]
                y = item[0][1]

                if (x < -1000 or x > 1000 or y < -1000 or y > 1000):
                    pass
                else:
                    arr.append(item[0])
    print("#{} {}".format(tc, energy))
#
# end = timeit.default_timer()
# print(end - start)