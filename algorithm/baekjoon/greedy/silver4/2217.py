"""
N개의 로프
- 로프는 들 수 있는 물체의 중량이 서로 다를 수 있다.
- 여러 개의 로프를 병렬로 연결하는 경우 w/k로 고르게 들 수있다.

로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량은?
"""
import sys

n = int(sys.stdin.readline().rstrip())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline().rstrip()))


def solution(rope):
    return max([value * (index + 1) for index, value in enumerate(sorted(rope, reverse=True))])


print(solution(rope))
