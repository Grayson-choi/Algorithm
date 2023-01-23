import sys
import itertools
from pprint import pprint

"""
5 2
60 50 70 80 90
"""

"""
3

"""

import sys
# sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
patients = list(map(int, input().split()))

for patient in patients:
    if patients[0] == max(patients):
        print(M + 1)
        break
    else:
        tmp = patients.pop(0)
        patients.append(tmp)
        M -= 1
        if M < 0:
            M = N - 1







