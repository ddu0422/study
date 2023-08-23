"""
일직선 상의 집들이 있다.
한 개의 안테나를 설치하는데 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다.
안테나는 집이 위치한 곳에만 설치할 수 있고, 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.

=== example ===
N = 4
house = 1, 5, 7, 9
5에 위치 (4 + 0 + 2+ 4) = 10

=> 중간에 위치하면 된다.
중간에 위치한 집이 왼쪽으로 가는 경우 왼쪽 집과 가까워지고 오른쪽 집과 동일한 거리만큼 멀어진다.
"""
n = int(input())
houses = list(map(int, input().split()))[:n]


def solution(houses):
    houses.sort()
    return houses[(len(houses) - 1) // 2]


print(solution(houses))
