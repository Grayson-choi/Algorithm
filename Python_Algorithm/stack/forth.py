"""
4
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
4 4 4 .
"""

T = int(input())

for test_case in range(1, T + 1):
    result = ""
    flag = 0
    stack = []
    li = input().split()
    for char in li:
        if char.isdecimal(): # 피연산자(숫자)인 경우
            stack.append(int(char))
        else:  # 연산자인 경우
            try:
                if char == ".":
                    break
                b = int(stack.pop())
                a = int(stack.pop())
                if char == "+":
                    stack.append(a + b)
                elif char == "-":
                    stack.append(a - b)
                elif char == "/":
                    stack.append(a // b)
                elif char == "*":
                    stack.append(a * b)
            except:
                flag = "error"
    if len(stack) == 1 and flag == 0:
        result = stack.pop()
        print("#{} {}".format(test_case, result))
    else:
        print("#{} error".format(test_case))



