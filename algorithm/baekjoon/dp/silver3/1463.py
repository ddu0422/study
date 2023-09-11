"""
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

연산을 사용하는 횟수의 최솟값을 출력

d[n]: n을 만들기 위한 연산의 최솟값
"""
n = int(input())


def solution(n):
    d = [10 ** 6 + 1] * (n + 1)
    d[0] = d[1] = 0

    for i in range(1, n + 1):
        if not i % 2:
            d[i] = min(d[i], d[i // 2] + 1)

        if not i % 3:
            d[i] = min(d[i], d[i // 3] + 1)
    
        d[i] = min(d[i], d[i - 1] + 1)
        
    return d[n]


print(solution(n))
