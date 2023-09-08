import sys

n = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)


def solution(numbers):
    return sorted(numbers, reverse=True)


print(*solution(numbers), sep='\n')
