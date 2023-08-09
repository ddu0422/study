"""
1. 짝수면 2로 나눈다.
2. 홀수면 3을 곱하고 1을 더한다.
3. 1이 될 때까지 반복한다.

주의)
1. 주어진 수가 1인 경우에는 0을 리턴한다.
2. 500번을 시도해도 1이 되지 않는 경우 -1을 리턴한다.
"""

def solution(num):
    if num == 1:
        return 0
    
    answer = 0

    for _ in range(500):
        num = num // 2 if num % 2 == 0 else num * 3 + 1        
        answer += 1

        if num == 1:
            return answer

    return -1


print(solution(6))