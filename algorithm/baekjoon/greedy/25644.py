"""
N일간의 주가 a1, a2, ..., an
i번째 날에 주식을 사고 j번째 날에 판다면 aj - ai 만큼의 이득
최대 이득은?
"""
n = int(input())
stocks = list(map(int, input().split()))[:n]


def solution(stocks):
    if len(stocks) <= 1:
        return 0
    
    answer = 0
    left = 0
    right = left + 1

    while right < len(stocks):
        if stocks[left] <= stocks[right]:
            answer = max(answer, stocks[right] - stocks[left])
            right += 1
        else:
            left = right
            right = left + 1

    return answer


def solution_rafactoring(stocks):
    answer = 0
    max_value = 0

    for value in stocks[::-1]:
        max_value = max(max_value, value)
        answer = max(answer, max_value - value)

    return answer


print(solution(stocks))
print(solution_rafactoring(stocks))
