"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

출력
#1 5
#2 5
#3 0
"""
import pprint

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    maze = []
    target_x, target_y = 0, 0
    start_x, start_y = 0, 0
    for i in range(n):
        row = list("".join(input()))
        maze.append(row)
        if "3" in row:
            x, y = row.index("3"), i
            target_x, target_y = x, y
        if "2" in row:
            x, y = row.index("2"), i
            start_x, start_y = x, y
    print()
    pprint.pprint(maze)
    print("s", start_x, start_y)
    print("t", target_x, target_y)
