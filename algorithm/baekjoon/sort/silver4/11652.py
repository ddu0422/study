import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(n):
    cards.append(int(sys.stdin.readline().rstrip()))


def solution(cards):    
    return sorted(Counter(cards).items(), key=lambda x: (-x[1], x[0]))[0][0]


print(solution(cards))
