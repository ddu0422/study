def solution(n):
    answer = ''

    while n:
        answer += str(n % 3)
        n //= 3

    return sum([int(value) * 3**(len(answer) - 1 - index) for index, value in enumerate(answer)])


def solution_refactor(n):
    answer = ''

    while n:
        answer += str(n % 3)
        n //= 3

    return int(answer, 3)


n = 45
print(solution(n))

n = 125
print(solution(n))