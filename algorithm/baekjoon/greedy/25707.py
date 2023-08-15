"""
구슬 N개 -> 서로 다른 수
두 구슬 사이슷 잇는 줄의 길이: 두 구슬에 적힌 수둘의 차의 절댓값
"""
n = int(input())
beads = list(map(int, input().split()))[:n]


def solution(beads):
    # 각 두 구슬의 차 + (처음 구슬의 마지막 구슬 차)
    answer = 0
    beads.sort()

    for i in range(len(beads)):
        answer += abs(beads[i] - beads[(i + 1) % len(beads)])

    return answer


print(solution(beads))
