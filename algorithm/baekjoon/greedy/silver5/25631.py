"""
N개의 마트료시카
i번째의 크기는 ai
i번째와 j번째를 고른 뒤 i번째를 j번째에 넣을 수 있어야함.
(단, j번째 마트료시카의 속이 비어있어야하고 i번째 마트료시카보다 j번째 마트료시카가 더 커야 함)

마트료시카를 최대한 합쳐서 정리
남아있는 마트료시카의 최소 개수는 얼마인가?
"""
n = int(input())
matryoshka = list(map(int, input().split()))[:n]


def solution(matryoshka):
    answer = 0
    checked = [False] * len(matryoshka)
    matryoshka.sort()

    for i in range(len(matryoshka)):
        if checked[i]:
            continue
        
        checked[i] = True
        current = matryoshka[i]

        for j in range(i + 1, len(matryoshka)):            
            if not checked[j] and current < matryoshka[j]:
                checked[j] = True
                current = matryoshka[j]

        answer += 1

    return answer

from collections import Counter


def solution_refactoring(matryoshka):
    # 마트료시카의 사이즈가 가장 많은 것이 남는 개수와 동일하다.
    # 어느 한 마트료시카를 선택한 경우 해당 마트료시카보다 크거나 작은 개수가 있다면 합쳐지기 때문이다.
    # 다만, 동일한 사이즈의 마트료시카는 합칠 수 없기 때문에 동일한 사이즈의 마트료시카가 남을 수 밖에 없다.
    return max(Counter(matryoshka).values())


print(solution(matryoshka))
print(solution_refactoring(matryoshka))
