import sys
import pprint
import queue
sys.stdin = open('input.txt', "r", encoding="utf-8")

T = int(input())

"""
1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)

2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)

3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)

4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.

5. 원자들의 이동 방향은 상(0), 하(1), 좌(2), 우(3)로 주어진다.

6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.

7. 원자들의 최초 위치는 서로 중복되지 않는다.

8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.

9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.

10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.
"""
#
for tc in range(1, T + 1):
    n = int(input())
    atoms = []
    board = [[0] * 1000 for _ in range(1000)]
    for i in range(n):
        wonja = list(map(int, input().split()))
        atoms.append(wonja)

    # 만나는게 없는 행성 찾기
    # print(atoms)
    result = 0
    stars = [0] * n
    check_list = []

    while True:
        for index, atom in enumerate(atoms):
            # print(index)
            level = 0
            x, y, dir, energy = atom[0], atom[1], atom[2], atom[3]

            if not atoms:
                break

            if dir == 0:
                # print("위")
                y = y + 0.5
                atoms[index] = (x, y, dir, energy)
                for idx, star in enumerate(atoms):
                    if idx != index:
                        if star[0] == x and star[1] == y:
                            # print("별 충돌")
                            result += star[3]
                            result += energy
                            # print("result")
                            atoms.pop(index)
                            atoms.pop(idx)
            elif dir == 1:
                # print("아래")
                y = y - 0.5
                atoms[index] = (x, y, dir, energy)
                for idx, star in enumerate(atoms):
                    if idx != index:
                        if star[0] == x and star[1] == y:
                            # print("별 충돌")
                            result += star[3]
                            result += energy
                            # print("result")
                            atoms.pop(index)
                            atoms.pop(idx)
            elif dir == 2:
                # print("왼쪽")
                x = x - 0.5
                atoms[index] = (x, y, dir, energy)
                for idx, star in enumerate(atoms):
                    if idx != index:
                        if star[0] == x and star[1] == y:
                            # print("별 충돌")
                            result += star[3]
                            result += energy
                            # print("result")
                            atoms.pop(index)
                            atoms.pop(idx)
            else:
                # print("오른쪽")
                x = x + 0.5
                atoms[index] = (x, y, dir, energy)
                for idx, star in enumerate(atoms):
                    if idx != index:
                        if star[0] == x and star[1] == y:
                            # print("별 충돌")
                            result += star[3]
                            result += energy
                            # print("result")
                            atoms.pop(index)
                            atoms.pop(idx)

        # print(atoms)
        # print(result)

        if len(atoms) == 0:
            break
        if not -1000 < atoms[0][0] < 1000:
            break
        if not -1000 < atoms[0][1] < 1000:
            break

    print("#{} {}".format(tc, result))


