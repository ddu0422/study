"""
총 레벨: N
각 레벨을 클리어할 때마다 점수가 주어짐

점수는 항상 양수

플레이어 점수: 각 레벨을 클리어하면서 얻은 점수의 합 (Online raking)
레벨을 난이도 순으로 배치
- 특정 레벨의 점수를 감소하여 각 레벨을 클리어할 때 주는 점수가 증가하게 만들려고 함.
- 점수를 내리는 것을 최소한으로 하는 방법?
"""
n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))


def solution(scores):
    answer = 0
    scores = scores[::-1]

    for index, value in enumerate(scores):
        if index + 1 == len(scores):
            break
        
        if value > scores[index + 1]:
            continue
        
        answer += abs(value - scores[index + 1]) + 1
        scores[index + 1] = value - 1
    
    return answer


print(solution(scores))
