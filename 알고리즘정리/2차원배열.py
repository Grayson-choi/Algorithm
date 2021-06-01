# row : 가로 길이
# col : 세로 길이

# board = [[0 for i in range(COLUM)] for j in range(ROW)]



# 2차원 배열 가장 자리에 0 추가하는 코드
# n은 배열의 크기
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0, 0)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):  # 4방향 탐색해서 가운데 값이 제일 높다면!
            cnt += 1
print(cnt)