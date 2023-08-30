import sys

n = int(sys.stdin.readline().rstrip())
balls = sys.stdin.readline().rstrip()[:n]


def solution(balls):
    r = balls.split('B')
    b = balls.split('R')

    # 전체 움직일 볼의 개수 - 왼쪽 or 오른쪽중에 있는 더 많은 동일한 볼의 개수를 제거 (움직이지 않음)
    return min(
        balls.count('R') - max(len(r[0]), len(r[-1])),
        balls.count('B') - max(len(b[0]), len(b[-1]))
    )


print(solution(balls))
