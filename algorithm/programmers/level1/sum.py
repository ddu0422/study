import itertools


def solution(numbers):
    return sorted(list(set([sum(numbers) for numbers in itertools.combinations(numbers, 2)])))


numbers = [1, 0, 0, 0]
print(solution(numbers))
