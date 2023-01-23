def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return answer
    
    garo = M - 1
    sero = M * (N - 1)
    answer = garo + sero
    return answer