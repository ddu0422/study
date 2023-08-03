"""
찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수 return
"""

def solution(numbers):
    return 45 - sum(numbers)


numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))