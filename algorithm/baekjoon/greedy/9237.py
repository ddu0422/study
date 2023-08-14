"""
n: 나무 묘목
하나를 심는데 걸리는 시간: 1일

Q: 각 묘목이 자라는데 며칠이 걸릴까?
A: 마지막 나무가 자란 날 (가장 작은 값, 처음값: 1일 -> O일?)

N: 묘목의 수
ti: 묘목이 자라는데 며칠이 걸리는 지

묘목이 자라는데 필요한 일 수: 4 3 3 2
각 묘목이 자라는데 필요한 일 수: 5 5 6 6
"""
n = int(input())
seeds = list(map(int, input().split()))[:n]


def solution(seeds):
    # 최소일을 구해야하므로 묘목이 자라는데 필요한 오래 걸리는 묘목부터 심기
    seeds = sorted(seeds, reverse=True)
    
    # 현재 일자 + 각 묘목이 자라는데 필요한 일 수 중 가장 큰 값
    return 1 + max([index + value + 1 for index, value in enumerate(seeds)])


print(solution(seeds))
