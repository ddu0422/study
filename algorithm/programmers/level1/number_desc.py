def solution(n):
    return int(''.join(sorted([s for s in str(n)], reverse=True)))


n = 118372
print(solution(n))