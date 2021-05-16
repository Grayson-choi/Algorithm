import sys
sys.stdin = open("input.txt", "r")

def update_visited(row, col, value):
    global right_down, left_down
    # 각 대각선의 시작 지점을 방문 체크.
    # \ 대각선 체크 : 대각선의 행과 열의 차에 N-1 의 값이 동일하다.
    right_down[row - col + (N - 1)] = value
    # / 대각선 체크 : 대각선의 행과 열의 합이 동일하다.
    left_down[row + col] = value


# 이미 둔 자리면 확인할 필요가 없음.
def check_visited(row, col):
    # 대각선 체크
    if right_down[row - col + (N - 1)] or left_down[row + col]:
        return False
    else:
        return True


def DFS(row, col, cnt):
    global max_cnt, color

    # 다음 row 확인.
    if col >= N:
        row += 1
        # 비트 연산자 사용해서 색깔 별로 시작 column을 다르게 함.
        col = color ^ (row % 2)
        # col = col % N # 시간 초과 발생.

    # 전체 확인 되었으면 종료.
    if row >= N:
        if max_cnt[color] < cnt:
            max_cnt[color] = cnt
        return

    # 둘 수 있는 자리, 비숍이 없는 자리 확인
    if DATA[row][col] and check_visited(row, col):
        update_visited(row, col, 1)
        DFS(row, col+2, cnt+1) # 비숍을 두고 다음 자리 방문 체크
        update_visited(row, col, 0)

    DFS(row, col+2, cnt) # 비숍을 두지 않고 다음 자리 방문 체크


N = int(input())
DATA = [list(map(int, input().split())) for _ in range(N)]
right_down = [0] * (2 * N) #  \ 대각선, 가로+세로 길이만큼 필요.
left_down = [0] * (2 * N) # / 대각선
max_cnt = [0, 0] # 검정 칸일 때와 흰색 칸일 때의 max 값

# 체스판을 나누지 않는 경우 O(2^(N*N)) : 시간 초과
# 체스판을 나누는 경우 O(2^(N/2 * N/2))

# 검정 체스판인 경우
color = 0
DFS(0, 0, 0) # row, col, cnt

# 흰색 체스판인 경우
color = 1
DFS(0, 1, 0)

print(max_cnt[0] + max_cnt[1])

