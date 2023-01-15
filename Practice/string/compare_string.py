"""
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
"""

T = int(input())

for test_case in range(1, T + 1):
    word = input()
    sentence = input()
    result = 0

    if word in sentence:
        result = 1
    else:
        result = 0
    print("#{} {}".format(test_case, result))