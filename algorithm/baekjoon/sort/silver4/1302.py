import sys
from collections import Counter


n = int(sys.stdin.readline().rstrip())
books = []
for _ in range(n):
    books.append(sys.stdin.readline().rstrip())


def solution(books):
    return sorted(Counter(books).items(), key=lambda x: (-x[1], x[0]))[0][0]


print(solution(books))
