"""
Nkg 배달
3kg 봉지
5kg 봉지
"""
n = int(input())


def solution(n):
    five = 0
    three = 0

    while n > 0:
        if n % 5 == 0:
            five += n // 5
            n %= 5
            break
        
        n -= 3
        three += 1

    if n < 0:
        return -1
    
    return five + three


print(solution(n))
