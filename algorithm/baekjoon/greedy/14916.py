"""
거스름 돈 동전의 최소 개수
거슬러 줄 수 없는 경우 -1
"""


n = int(input())


def solution(n):
    five_coin = 0
    two_coin = 0

    while n > 0:
        if not n % 5:
            five_coin = n // 5
            break

        n -= 2
        two_coin += 1
    
    if n < 0:
        return -1

    return two_coin + five_coin


print(solution(n))
