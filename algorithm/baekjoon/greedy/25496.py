"""
N: 만들 수 있는 장신구
Ai : 각각의 장신구를 만들면 누적되는 피로도

피로도가 200미마인 경우 장신구 제작 가능
현재 쌓인 피로도가 P일 대, 제작할 수 있는 장신구의 최대 개수는?
"""
p, n = map(int, input().split())
fatigue = list(map(int, input().split()))[:n]


def solution(p, fatigue):
    fatigue.sort()
    total = 200 - p
    answer = 0

    for value in fatigue:
        if total <= 0:
            break
        
        total -= value
        answer += 1

    return answer


print(solution(p, fatigue))
