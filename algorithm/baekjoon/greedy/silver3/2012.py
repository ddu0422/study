"""
학생들은 N명 중에 몇 등 할 지 예상 등수를 적었다.
각 사람이 제출한 에상 등수를 바탕으로 임의로 등수를 매기기로 했다.

A등으로 예상하였는데 실제 등수가 B등이 될 경우
불만도 abs(A-B)이다.
불만도의 총 합의 최소는?

예상 순으로 정렬한다.
1 1 2 3 5
0 1 1 1 0
"""
import sys
n = int(sys.stdin.readline().rstrip())
rank = []
for _ in range(n):
    rank.append(int(sys.stdin.readline().rstrip()))


def solution(rank):
    answer = 0
    rank.sort()

    for index, value in enumerate(rank):
        answer += abs((index + 1) - value)
    
    return answer


print(solution(rank))
