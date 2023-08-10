import math


def solution(s):
    n = len(s)
    return ''.join(list(s)[(n - 1) // 2:math.ceil((n + 1) / 2)])


s = 'abcde'
print(solution(s))
