import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(cards, numbers):
    counts = [0] * (10000000 * 2 + 2)

    for number in cards:
        counts[number] += 1

    return [counts[number] for number in numbers]


print(*solution(cards, numbers))
