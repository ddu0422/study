def solution(food):
    answer = ''.join(str(index) * (value // 2) for index, value in enumerate(food))

    return answer + '0' + answer[::-1]


food = [1, 3, 4, 6]
print(solution(food))