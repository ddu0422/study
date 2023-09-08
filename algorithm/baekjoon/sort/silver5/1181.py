import sys

n = int(sys.stdin.readline().rstrip())
text = []
for _ in range(n):
    text.append(sys.stdin.readline().rstrip())


def solution(text):
    return sorted(set(text), key=lambda x: (len(x), x))


print(*solution(text), sep='\n')
