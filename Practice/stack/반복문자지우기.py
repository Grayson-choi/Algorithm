T = int(input())

for test_case in range(1, T + 1):
    stack = []
    word = input()
    word += "!"
    for char in word:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print("#{} {}".format(test_case, len(stack) - 1))