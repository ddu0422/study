"""
각 접시: 시계방향으로 1부터 N까지 번호
- i번째 접시에는 ai가 적혀있다. (N번 접시 이후 -> 1번 접시)

적절히 원판을 끊어 오름차순 배열을 만드는 것.
최소 횟수는?
"""
n = int(input())
numbers = list(map(int, input().split()))[:n]


def solution(numbers):
    answer = 0
    numbers += [numbers[0]]

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            answer += 1
            
    return answer


print(solution(numbers))
