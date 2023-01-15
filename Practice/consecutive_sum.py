def consecutive_sum(start, end):
    # 코드를 작성하세요
    sum = 0
    if start == end:
        return start
    for i in range(start,end+1):
        sum += i
    return sum

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))