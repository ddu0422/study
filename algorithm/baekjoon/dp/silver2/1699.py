n = int(input())


def solution(n):
    d = list(range(n + 1))

    for i in range(1, n + 1):
        for j in range(int(i ** .5), 0, -1):
            if i == j * j:
                d[i] = 1
            elif i > j * j:
                d[i] = min(d[i - j * j] + d[j * j], d[i])

    return d[n]


print(solution(n))
