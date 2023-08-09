"""
하샤드 수: x의 자릿수의 합으로 x가 나누어져야 함.
"""

def solution(x):
    return not x % sum(list(map(int, str(x))))


print(solution(10))