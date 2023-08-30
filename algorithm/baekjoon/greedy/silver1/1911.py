"""
N개의 물웅덩이
물웅덩이를 덮을 수 있는 길이 L
물웅덩이를 덮기 위해 필요한 널빤지의 최소 개수

=== example ===
3 3
1 6
13 17
8 12

끝 위치는 포함하지 않는다.

111222. // 널빤지
.MMMMM. // 웅덩이
0123456 // 좌표
"""
import sys
from math import ceil

n, l = map(int, sys.stdin.readline().rstrip().split())
pools = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    pools.append((start, end))


def solution(l, pools):    
    # 끝에서 부터 놓는다.
    pools = sorted(pools, key=lambda x: -x[1])
    standard = pools[0][-1]
    answer = 0

    # 다음 물웅덩이가 올 때 이미 놓인 경우와 놓이지 않은 경우를 구분한다.
    # 놓이지 않은 경우는 끝에서 놓는 방식과 동일하다.
    # 하지만 놓인 경우는 끝에서 놓았을 때 널빤지의 위치를 끝으로 지정한다.
    for start, end in pools:
        count = ceil((min(end, standard) - start) / l)
        length = l * count
        answer += count
        standard = min(end, standard) - length    
    
    return answer


print(solution(l, pools))
