def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))


strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))
