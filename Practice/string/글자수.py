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
    ch = {}

    for char in sentence:
        if char in word:
            if not char in ch:
                ch[char] = 1
            else:
                ch[char] += 1
    result = max(ch.values())
    print("#{} {}".format(test_case, result))

