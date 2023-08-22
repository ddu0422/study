"""
학교에 간 뒤 최소 시간동안 머물다가 모든 팬들과 한 번 씩 인사를 하고 학교를 떠남.

=== example ===
A: 1, 2, 3, 4
B: 2, 3, 4
C: 2, 3, 4, 5
=> 학교에 가자마자 한번에 인사할 수 있음.

A: 1, 2, 3, 4
B: 5, 6
=> 4, 5 (학교에 머무는 시간의 총 합은 1)
A에게 인사 후 B에게 인사하기 위해 시간이 필요함.
"""
import sys

n = int(sys.stdin.readline().rstrip())
times = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    times.append((start, end))


def solution(times):
    # 시작시간이 끝 시간보다 큰 경우 이어줘야한다.
    """
    3
    1 2
    2 5
    3 4
    """
    # 위에 경우 1 2 / 3 4 사이에서 기다려야함.
    start = max(times, key=lambda x: x[0])[0]
    end = min(times, key=lambda x: x[1])[1]

    if start > end:
        return start - end
    
    return 0


print(solution(times))
