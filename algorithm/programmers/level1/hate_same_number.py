def solution(arr):
    answer = []

    for number in arr:
        if not answer or answer[-1] != number:
            answer.append(number)
    
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
