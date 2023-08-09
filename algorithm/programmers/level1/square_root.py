def solution(n):
    x = int(n**(1/2))
    return (x + 1)**2 if x == n**(1/2) else -1


n = 121
print(solution(n))