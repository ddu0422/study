import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
scores = []
for _ in range(n):
    no, g, s, b = map(int, sys.stdin.readline().rstrip().split())
    scores.append([no, g, s, b])


def solution(scores, k):
    ranks = [0] * n
    rank = 1
    scores = sorted(scores, key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    ranks[scores[0][0] - 1] = rank

    for i in range(1, len(scores)):
        rank += 1
        if scores[i - 1][1:] == scores[i][1:]:
            ranks[scores[i][0] - 1] = ranks[scores[i - 1][0] - 1]
        else:
            ranks[scores[i][0] - 1] = rank

    return ranks[k - 1]

print(solution(scores, k))
