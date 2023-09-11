"""
0번째 0
1번째 1
2번째부터는 바로 앞 두 피보나치 수의 합
"""
import sys

n = int(sys.stdin.readline().rstrip())


def solution(n):
    a, b = 0, 1

    for i in range(2, n + 1):
        if not i % 2:
            # 미리 나누어서 저장해야한다.
            # 큰 숫자가 되면 비트를 많이 사용하기 때문에 연산 속도가 오래걸린다.
            a = (a + b) % 1000000007
        else:
            b = (a + b) % 1000000007

    return a if not n % 2 else b


print(solution(n))
