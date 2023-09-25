"""
Ai 이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다.

미로의 가장 왼쪽 끝에 있고, 가장 오른쪽 끝으로 가려고 한다.
최소 몇 번 점프를 해야 갈 수 있는지 구하시오.

가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력

d[n]: n칸에 도달했을 때, 최소 점프 횟수.

10
1 2 0 1 3 2 1 5 4 2

10
1 0 0 0 0 0 0 0 1 0
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(numbers):
    # 출발 지역이 오른쪽 끝인 경우
    if len(numbers) == 2:
        return 0
    
    # 출발을 할 수 없는 경우
    if not numbers[1]:
        return - 1

    d = [0] * len(numbers)

    for i in range(1, len(numbers)):
        for j in range(1, numbers[i] + 1):
            # 범위를 벗어나는 경우 / 이미 방문한 경우
            if i + j > n or d[i + j]:
                continue

            # 처음을 제외하고 현재 위치에 도달할 수 없는 경우
            if i != 1 and not d[i]:
                continue

            if d[i + j] < d[i] + 1:
                d[i + j] = d[i] + 1

    return d[-1] or -1


print(solution(numbers))
