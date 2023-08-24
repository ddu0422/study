"""
N: 빨대의 개수
3개의 빨대를 선택 => 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값

삼각형 조건
가징 긴 변의 길이가 다른 두 변의 길이의 합보다 작은 경우
"""
import sys

n = int(sys.stdin.readline().rstrip())
edges = []
for _ in range(n):
    edges.append(int(sys.stdin.readline().rstrip()))


def solution(edges):
    """
    변 a, b, c, d가 주어진 경우 (a <= b <= c <= d)
    가장 큰 변(d)을 기준으로 b + c <= d(삼각형이 아니고)이면서 a < c이기 때문에 a + b > d인 경우는 존재하지 않는다.
    즉, 가장 "인접"한 세 점이 가장 큰 삼각형을 만들 수 있다.
    """
    answer = -1
    edges = sorted(edges, reverse=True)

    for i in range(len(edges) - 2):
        if edges[i + 2] + edges[i + 1] > edges[i]:
            answer = max(answer, edges[i] + edges[i + 1] + edges[i + 2])
            break
      
    return answer


print(solution(edges))
