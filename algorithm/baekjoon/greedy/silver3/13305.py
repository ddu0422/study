"""
N: 도시 개수
일직선 도로 위에 있다.
제일 왼쪽 도시에서 제일 오른쪽 도시로 자동차를 이용하여 이동
인접한 두 도시 사이의 도로는 길이가 다를 수 있다. (단위는 km)

도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용
각 도시에는 하나의 주유소가 있다. 도시마다 리터당 가격이 다름.

=== example ===
4
2 3 1
5 2 4 1

1번 도시에서 2km를 넣고 달린다. => 5 * 2 = 10
2번 도시에서 4km를 넣고 달린다. => 2 * 4 = 8
"""
import sys

n = int(sys.stdin.readline().rstrip())
distance = list(map(int, sys.stdin.readline().rstrip().split()))[:n - 1]
city = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(distance, city):
    # 이전 도시 중 가장 싼 곳과 현재 도시를 비교하여 더 싼 곳의 기름을 넣는다.
    cheapest = city[0]
    answer = 0

    for index, value in enumerate(distance):
        if cheapest > city[index]:
            cheapest = city[index]
        answer += value * cheapest
            
    return answer


print(solution(distance, city))
