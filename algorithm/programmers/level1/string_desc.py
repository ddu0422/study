"""
대문자는 소문자보다 작음
"""

def solution(s):
    return ''.join(sorted(list(s), reverse=True))


s = "Zbcdefg"
print(solution(s))