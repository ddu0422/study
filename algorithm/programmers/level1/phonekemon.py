"""
N마리 폰켓몬 중 N/2마리 가져갈 수 있음
동일한 폰켓몬 존재 / 최대한 많은 폰켓몬을 가져야함
"""


def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


nums = [3, 1, 2, 3]
print(solution(nums))
