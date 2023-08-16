"""
기타줄의 개수: N
브랜드 개수: M
각 줄은 6개 패키지 가격 / 낱개 가격

기타줄 N개를 사는데 최소한의 비용은?
(N개를 오버해서 구매하지만 값이 싼 경우가 있을 수 있다.)
"""
n, m = map(int, input().split())
brands = []
for _ in range(m):
    package, ea = map(int, input().split())
    brands.append((package, ea))


def solution(n, brands):
    packages = min(brands, key=lambda x: x[0])[0]
    each_others = min(brands, key=lambda x: x[1])[1]
    
    return min(
        ((n // 6) + 1) * packages,                   # 패키지로만 구매하는 경우
        (n // 6) * packages + (n % 6) * each_others, # 패키지와 낱개를 혼합하여 구매하는 경우
        n * each_others                              # 낱개로만 구매하는 경우
    )


print(solution(n, brands))
