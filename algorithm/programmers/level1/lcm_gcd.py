def solution(n, m):
    result = gcp(n, m)

    return [result, n * m // result]


def gcp(a, b):
    a, b = max(a, b), min(a, b)

    while b:
        r = a % b
        a = b
        b = r

    return a


n, m = 2, 5
print(solution(n, m))