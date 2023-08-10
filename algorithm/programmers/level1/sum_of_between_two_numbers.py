def solution(a, b):
    a, b = min(a, b), max(a, b)
    return sum([number for number in range(a, b + 1)])


a, b = 5, 3
print(solution(a, b))
