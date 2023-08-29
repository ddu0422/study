"""
N개의 회의에 대하여 회의실 사용표를 만든다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져있다.
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수를 찾아보자.

단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
(시작 시간과 끝나는 시간이 동일한 경우 시작하자마자 끝나는 것으로 생각한다.)

0 6
1 4
2 13
3 5
3 8
5 7
5 8
6 10
8 11
8 12
12 14

1 4
7 7
4 7
3 7
5 7
6 7
"""
import sys

n = int(sys.stdin.readline().rstrip())
times = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    times.append((start, end))


def solution(times):
    answer = 0
    end_time = 0
    # 끝나는 순으로 오름차순을 정렬하게 되면, 시작 시간에 상관없이 앞 쪽 회의를 진행할 수 있다.
    # 시작 시간과 끝나는 시간이 동일한 경우가 있기 때문에 시작 시간을 오름차순으로 정렬해야한다.
    """
    예시
    3
    1 3
    3 3
    2 3
    """
    times = sorted(times, key=lambda x: (x[1], x[0]))
    
    for start, end in times:
        if end_time <= start:
            answer += 1
            end_time = end
    
    return answer


print(solution(times))
