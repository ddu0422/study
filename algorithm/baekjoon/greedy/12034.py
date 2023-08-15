"""
모든 품목을 25% 할인된 가격으로 판매
정상가는 4의 배수인 정수 / 할인된 가격도 정수

할인가격과 정상가격을 따로 구분하지 않고 오름차순으로 정렬한 뒤 순서대로 출력
할인 가격표는?

=== example ===
15 20 60 75 80 100

15 60 75
"""
t = int(input())


def solution(prices):
    answer = []
    prices = sorted(prices, reverse=True)

    for index, price in enumerate(prices):
        if price:
            discount_price = prices.index(int(price * 0.75))
            answer.append(prices[discount_price])
            prices[index] = 0
            prices[discount_price] = 0
    
    return sorted(answer)


for i in range(1, t + 1):
    n = int(input())
    prices = list(map(int, input().split()))[:n * 2]
    print(("Case #{}: " + ' '.join([str(value) for value in solution(prices)])).format(i), end="\n")
