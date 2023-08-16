"""
30의 배수가 되기 위한 조건
1. 모든 수의 합이 3의 배수일 것
2. 0이 포함되어 있어야할 것
"""
n = int(input())


def solution(n):
    numbers = sorted(list(map(int, str(n))), reverse=True)
    
    if 0 in numbers and sum(numbers) % 3 == 0:
        return numbers
    
    return [-1]


print(*solution(n), sep='')
