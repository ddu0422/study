"""
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 / 영어점수가 같으면 수학 점수가 감소하는 순으로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
"""
import sys

n = int(sys.stdin.readline().rstrip())
scores = []
for _ in range(n):
    input = sys.stdin.readline().rstrip().split()
    scores.append((input[0], *list(map(int, input[1:]))))


def solution(scores):
    return map(lambda x: x[0], sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0])))


print(*solution(scores), sep='\n')
