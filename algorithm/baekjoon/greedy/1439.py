"""
문자열의 모든 숫자를 전부 같게 해야함.
문자열을 뒤집을 최소 횟수를 구하시오.

0/1 뒤집기 중 둘 중 더 작은 숫자 개수
"""

s = input()


def solution(s):
    queue = []

    for i in s:
        if queue[-1:] != [i]:
            queue.append(i)

    return min(queue.count('0'), queue.count('1'))


print(solution(s))