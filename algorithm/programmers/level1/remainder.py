"""
자연수 n
n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x
"""
def solution(n):
    n -= 1
    answer = n

    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            answer = i
            break

    return answer


print(solution(10))