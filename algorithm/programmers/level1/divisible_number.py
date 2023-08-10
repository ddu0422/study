def solution(arr, divisor):
    return sorted(filter(lambda x: not (x % divisor), arr)) or [-1]


arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))
