"""
서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수
"""
import itertools


def solution(nums):
    return len(
        [
            'O' for case in itertools.combinations(nums, 3)
            if len(get_prime(sum(case))) == 1
        ]
      )


def get_prime(number):
    return [i for i in range(1, int(number**(1/2) + 1)) if number % i == 0]


nums = [1, 2, 7, 6, 4]
print(solution(nums))