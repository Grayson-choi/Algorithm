def fib_tab(n):
    # 코드를 작성하세요.
    list = [0,1,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    count = 3
    while count < n:
        list.append(list[count - 2] + list[count - 1])
        count += 1 
    return list[n - 2] + list[n - 1]
# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))