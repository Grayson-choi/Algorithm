import sys
import itertools
from pprint import pprint

"""
(3+5)*2
"""

"""
35+2*
"""

# import sys
# sys.stdin=open("input.txt", "r")

fomular = input()
stack = []
result = ""

for char in fomular:
    if char.isdecimal(): # 숫자인지 확인
        result += char
    else:
        if char == "(":
            stack.append(char)
        elif char == "*" or char == "/":
            while stack and (stack[-1] == '*' or stack[-1] == "/"):
                result += stack.pop()
            stack.append(char)
        elif char == "+" or char == "-":
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.append(char)
        elif char == ")":
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)




