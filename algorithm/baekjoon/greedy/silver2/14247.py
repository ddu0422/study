"""
산에는 n개의 나무가 있다.
영선이는 하루에 한 나무씩 n일 산에 오르며 나무를 자른다.

나무들은 매우 빠르게 자란다.
나무의 처음 길이와 하루에 자라는 양이 주어졌을 때, 영선이가 얻을 수 있는 최대 나무양을 구하시오.

자른 이후에도 나무는 0부터 다시 자라기 때문에 같은 나무를 여러 번 자를 수 있다.

=== example ===
1 3 2 4 6
2 7 3 4 1

3 + 7 * 4 = 31
4 + 4 * 3 = 16
2 + 3 * 2 = 8
1 + 2 * 1 = 3
6 + 1 * 0 = 6
"""
import sys

n = int(sys.stdin.readline().rstrip())
h = list(map(int, sys.stdin.readline().rstrip().split()))
a = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(h, a):
    trees = sorted([(height, velocity) for height, velocity in zip(h, a)], key=lambda x: (x[1], x[0]))
    return sum([value[0] + value[1] * index for index, value in enumerate(trees)])


print(solution(h, a))
