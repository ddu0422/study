"""
1. 계단을 한 계단 씩 또는 두 계단씩 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안된다.
3. 마지막 도착 계단은 반드시 밟아야한다.

d[n]: n번째 계단을 밟았을 때 최대 점수

 OX | O
OXO | O

1. 직전 계단을 밟지 않은 경우
d[i - 2] + a[i]이다.

2. 직전 계단을 밟은 경우

d[i - 1]이 아닌 d[i - 3]인 이유는 d[i - 1]에서 직전 계단을 밟았을 때, 최대 점수일 수 있기 때문이다.
d[i - 3]의 최대 점수에서 a[i - 1] 계단과 a[i] 계단을 밟아야한다.
"""
import sys

n = int(sys.stdin.readline().rstrip())
a = [0]
for _ in range(n):
    score = int(sys.stdin.readline().rstrip())
    a.append(score)


def solution(n, a):
    if n == 1:
        return a[1]

    d = [0] * (n + 1)
    d[1] = a[1]
    d[2] = a[1] + a[2]

    for i in range(3, n + 1):
        d[i] = max(d[i - 2], d[i - 3] + a[i - 1]) + a[i]

    return d[n]


print(solution(n, a))
