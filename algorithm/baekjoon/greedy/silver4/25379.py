"""
A: 음이 아닌 정수 배열
인접한 두 수를 교환하는 시행을 원하는 만큼 가능
홀수와 짝수가 인접한 경우 최대 1번 등장하도록 하는 시행의 최소 횟수는?

=== example ===
A = [4, 5, 1 ,0]
  = [4. 0, 5, 1]이 되는 경우 홀수와 짝수가 인접한 경우 최대 1번이 됨.
"""
import sys
from copy import deepcopy

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(array):
    left1 = 0
    right1 = len(array) - 1
    left2 = 0
    right2 = len(array) - 1
    array1 = deepcopy(array)
    array2 = deepcopy(array)
    answer1 = 0
    answer2 = 0

    while left1 < right1:
        while left1 < len(array1) and array1[left1] % 2 == 0:
            left1 += 1

        while right1 > 0 and array1[right1] % 2 != 0:
            right1 -= 1

        if left1 < right1:
            array1[left1], array1[right1] = array1[right1], array1[left1]
            answer1 += right1 - left1


    while left2 < right2:
        while left2 < len(array2) and array2[left2] % 2 != 0:
            left2 += 1

        while right2 > 0 and array2[right2] % 2 == 0:
            right2 -= 1

        if left2 < right2:
            array2[left2], array2[right2] = array2[right2], array2[left2]
            answer2 += right2 - left2

    
    return min(answer1, answer2)


print(solution(array))


def solution_refactor(array):
    odd = 0
    even = 0

    for value in array:
        if value & 1:
            odd += 1
        else:
            even += odd

    return min(even, (len(array) - odd) * odd - even)


print(solution_refactor(array))