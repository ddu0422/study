"""
0 1 1 2 3 5 8

f(0) = f(0)
f(1) = f(1)        = 1f(1) + 0f(0)
f(2) = f(1) + f(0) = 1f(1) + 1f(0)
f(3) = f(2) + f(1) = 2(f1) + 1f(0)
f(4) = f(3) + f(2) = 3f(1) + 2f(0)
f(5) = f(4) + f(3) = 5f(1) + 3f(0)
f(6) = f(5) + f(4) = 8f(1) + 5f(0)

=> 0과 1의 개수가 피보나치 수열을 이룬다.
"""
import sys

t = int(sys.stdin.readline().rstrip())


def solution(n):
    if n == 0:
        return [1, 0]
    
    a, b = 0, 1

    for i in range(2, n + 1):
        if not i % 2:
            a = a + b
        else:
            b = b + a

    return [a, b] if n % 2 else [b, a]


for _ in range(t):
    print(*solution(int(sys.stdin.readline().rstrip())))
