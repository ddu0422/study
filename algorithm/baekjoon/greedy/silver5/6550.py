"""
문자열 s와 t
s가 t의 부분 문자열인지 판단

부분문자열: t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우
"""
import sys


def solution(s, t):
    index = 0

    for alpha in t:
        if s[index] == alpha:
            index += 1

        if index == len(s):
            return 'Yes'
    
    return 'No'


for line in sys.stdin:
    s, t = line.rstrip().split()
    print(solution(s, t))
