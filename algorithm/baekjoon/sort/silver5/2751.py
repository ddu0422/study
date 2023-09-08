"""
주의사항) "절댓값"이 1,000,000보다 작거나 같은 정수
-1,000,000 ~ 1,000,000
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] * (2000001 + 1)
for _  in range(n):
    number = int(sys.stdin.readline().rstrip())
    numbers[number + 1000000] += 1


def solution(numbers):
    return [index - 1000000 for index, value in enumerate(numbers) if value]


print(*solution(numbers), sep="\n")
