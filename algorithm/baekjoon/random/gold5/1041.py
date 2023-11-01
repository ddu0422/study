import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(n, numbers):
    # 크기가 1인 경우는 1x1의 정육면체를 만들 수 있으며, 가장 큰 값을 바닥에 놓는다면 모든 면의 합이 최솟값이다.
    if n == 1:
        return sum(sorted(numbers)[:5])
    
    # 어느 한 면을 기준으로 최솟값들을 정한다.
    # 서로 마주보는 면은 사용할 수 없기에 마주보는 값들 중 숫자가 작은 값을 구한다.
    num1, num2, num3 = sorted(
        [
            min(numbers[0], numbers[5]),
            min(numbers[1], numbers[4]),
            min(numbers[2], numbers[3])
        ]
    )

    result = [
        # 최상층을 제외(n - 1)하고 네 면(4)을 기준으로 각 층마다 (N - 2)씩 존재 + 최상층에선 (n - 2)^2개 존재
        (n - 2) * 4 * (n - 1) + (n - 2) ** 2, # 1개 짜리
        # 최상층을 제외(n - 1)하고 각 층마다 4개씩 존재 + 최상층에선 네 면(4)을 기준으로 n - 2개씩 존재
        4 * (n - 1) + (n - 2) * 4,            # 2개 짜리
        # 최상층에만 존재하며 항상 4개만 존재
        4                                     # 3개 짜리
    ]

    return num1 * result[0] + (num1 + num2) * result[1] + (num1 + num2 + num3) * result[2]


print(solution(n, numbers))
