"""
책은 차례대로 박스에 넣어야한다.

n: 책의 개수
m: 박스에 넣을 수 있는 최대 무게
"""
n, m = map(int, input().split())
weights = []

for _ in range(min(n, 1)):
    weights = list(map(int, input().split()))[:n]


def solution(m, weights):
    if not len(weights):
        return 0
    
    answer = 1

    total = 0
    
    for weight in weights:
        total += weight

        if total > m:
            answer += 1
            total = weight
    
    return answer


print(solution(m, weights))
