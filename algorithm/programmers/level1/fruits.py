def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        box = score[i:i + m]
        
        if len(box) == m:
            answer += box[-1] * m

    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
