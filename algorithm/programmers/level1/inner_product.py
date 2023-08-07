def solution(a, b):
    return sum([value1 * value2 for value1, value2 in zip(a, b)])

a = [-1,0,1]
b = [1,0,-1]

print(solution(a, b))