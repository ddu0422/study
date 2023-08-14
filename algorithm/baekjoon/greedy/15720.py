"""
B, C, D가 각각 존재하는 경우 10% 할인

B: 버거의 개수
C: 사이드 메뉴 개수
D: 음료의 개수

최저가 출력

=== example ===
3 3 2
2000 3000 2500
800 1300 1000
500 1000

12100
11170

3000 + 1300 + 1000 => 5300 * 0.9 = 4770
2500 + 1000 + 500 => 4000 * 0.9 = 3600
2000 + 800 = 2800
"""
b, c, d = map(int, input().split())
menus = []
for _ in range(3):
    menus.append(list(map(int, input().split())))


def solution(menus):
    minimum_sets = 1001
    price = 0
    discount_price = 0

    # 1. 오름차순으로 정렬한다.
    # 2. 세트를 만들 수 있는 개수를 구한다.
    for index, value in enumerate(menus):
        menus[index] = sorted(value, reverse=True)
        minimum_sets = min(minimum_sets, len(value))

    for menu in menus:
        for index, value in enumerate(menu):
            price += value
            if index < minimum_sets:
                discount_price += value * 0.9
            else:
                discount_price += value

    return [price, discount_price]


for price in solution(menus):
    print(int(price))
    