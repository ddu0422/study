"""
음이 아닌 정수 N (0, 양의 정수)
서로 다른 정수 (M >= 1)개의 팩토리얼 합으로 나타낼 수 있는지 알아보는 프로그램
-> 0! = 1
"""
import itertools


n = int(input())


def solution(n):
    factories = [1]

    for i in range(1, 21):
        factories.append(factories[i - 1] * i)

    for i in range(1, len(factories) + 1):
        for value in itertools.combinations(factories, i):
            if n == sum(value):
                return 'YES'

    return 'NO'


print(solution(n))
