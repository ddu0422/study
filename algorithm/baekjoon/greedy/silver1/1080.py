"""
행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하시오.
행렬의 연산은 3x3 크기의 부분 행렬의 모든 원소를 뒤집는 것이다.

100
000
011

011
000
100
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n * 2):
    row = list(sys.stdin.readline().rstrip())[:m]
    matrix.append(row)


def solution(matrix):
    answer = 0
    a = matrix[:len(matrix) // 2]
    b = matrix[len(matrix) // 2:]

    # 크기에 상관없이 처음부터 동일한 경우는 변경할 필요가 없다.
    if a == b:
        return answer

    # 3x3 부분행렬을 사용할 수 없는 경우 변경할 수 없다.
    if len(a) < 3 or len(a[0]) < 3:
        return -1

    # 0,0부터 3x3 부분행렬로 변경하며 비교한다.
    for y in range(len(a[0]) - 2):
        for x in range(len(a) - 2):
            if a[x][y] != b[x][y]:
                for k in range(3):
                    for l in range(3):
                        a[x + k][y + l] = '0' if int(a[x + k][y + l]) else '1'
                answer += 1
    
    # 동일한 행렬이면 변경 횟수를 반환하고, 동일하지 않으면 -1을 반환한다.
    return answer if a == b else -1


print(solution(matrix))
