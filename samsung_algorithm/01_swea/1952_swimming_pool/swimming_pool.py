import sys
sys.stdin = open('input.txt')

def dfs(exp, idx):
    global min_val
    if idx >= 12:
    #11월과 12월이 세달 이용권을 할 때가 있을 것이기 때문에, 12일때가 아닌 12보다 클 때라고 설정해줌
    #사실 12월은 무조건 세 달이 아닌 한 달혹은 일 이용권을 하는 것이 이득이겠지만 그에 따른 처리를 해주는 것보다
    #이렇게 처리를 해주는 편이 훨씬 간편합니다.
        if min_val > exp:
            min_val = exp
        return
    if month[idx]*ticket[0] < ticket[1]: #한 달을 모두 일 이용권으로 사용하는게 한 달이용권보다 쌀 때
        dfs(exp+month[idx]*ticket[0], idx+1)
    else: # 한달 이용권이 더 쌀 때
        dfs(exp+ticket[1], idx+1)
    if month[idx]: #만약 그 달에 0일이면 세 달 이용권을 시작하지 않아도 되니까 솎아주기
        dfs(exp+ticket[2], idx+3) #세 달 이용권일 때 idx 처리 주의!


T = int(input())

for test_case in range(1, T+1):
    ticket = list(map(int, input().split()))
    month = list(map(int, input().split()))
    min_val = ticket[3] #일년 이용권을 최소값으로 설정해주기
    dfs(0,0)
    print('#{} {}'.format(test_case, min_val))

# 11:07:19 실행이 완료되었습니다. 실행 시간 : 0.16910s
