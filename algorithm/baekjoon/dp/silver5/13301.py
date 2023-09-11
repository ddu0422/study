"""
피보나치수열
d[n] = d[n - 1] + d[n - 2]

정사각형 2개가 합쳐 다음 정사각형과 동일하다.
80번째 사각형은 81번째 정사각형과 80번째 정사각형으로 이루어져있다.
"""
n = int(input())


def solution(n):
    d = [0] * (80 + 2)
    d[1] = 1

    for i in range(2, n + 2):
        d[i] = d[i - 1] +  d[i - 2]


    return 2 * d[n + 1] + 2 * d[n]


print(solution(n))
