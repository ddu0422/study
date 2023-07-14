def solution(ingredient):
    answer = 0

    queue = []

    for element in ingredient:
        queue.append(element)

        if queue[-4:] == [1, 2, 3, 1]:
            answer += 1

            for _ in range(4):
                queue.pop()
    
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

print(solution(ingredient))