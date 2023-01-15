# -*- coding: utf-8 -*-
T = [73, 74, 75, 71, 69, 72, 76, 73]

stack = []
answer = [0] * len(T)

for i, cur in enumerate(T):
    idx = i
    while stack and T[stack[-1]] < cur:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

print(answer)