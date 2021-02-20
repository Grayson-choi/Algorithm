# n번째 피보나치 수를 담는 사전
fib_cache = {}


def fib_memo(n):
    # 코드를 작성하세요.

    if n == 1:
        return 1
    if n == 2:
        return 1

    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = fib_memo(n-2) + fib_memo(n-1)
    return fib_cache[n]


# 테스트
print(fib_memo(10))
print(fib_memo(50))
print(fib_memo(100))
