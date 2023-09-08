"""
N개의 카드를 가지고 있다.
정수 M개가 주어졌을 때, 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램을 작성하시오.

N: 카드의 개수 (1 <= N <= 500,000)
둘째 줄: 카드의 숫자 (-10,000,000 <= X <= 10,000,000)
M: 카드의 개수 (1 <= M <= 500,000)
넷째 줄: 상근이가 가지고 있는 숫자 카드인지 아닌지를 판단해야할 카드의 숫자 (-10,000,000 <= X <= 10,000,000)
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
numbers2 = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(numbers1, numbers2):
    # 1~10,000,000까지 순차대로 들어감.
    # -10,000,000~-1은 배열의 뒤에서부터 순차대로 들어감
    numbers = [0] * (10000000 * 2 + 2)

    for number in numbers1:
        numbers[number] += 1

    return [1 if numbers[value] else 0 for value in numbers2]


print(*solution(numbers1, numbers2))
