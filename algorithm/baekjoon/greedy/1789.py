n = int(input())


def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n < (i * i + i) // 2:
            break
        answer = i
    
    return answer


print(solution(n))
