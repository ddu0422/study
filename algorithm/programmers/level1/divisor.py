"""
약수의 개수가 짝수인 경우 => +
약수의 개수가 홀수인 경우 => -
"""

def solution(left, right):
    answer = 0
    
    for number in range(left, right + 1):
        count = count_divisor(number)
        if count % 2 == 0:
            answer += number
        else:
            answer -= number

    return answer


def count_divisor(number):
    count = 0
    
    for i in range(1, int(number**(1/2)) + 1):
        if number % i == 0:
            if i == number**(1/2):
                count += 1
            else:
                count += 2

    return count


def solution_refactor(left, right):
    return sum(
        [-number if int(number**(1/2)) == number**(1/2) else number for number in range(left, right + 1)]
    )


print(solution(24, 27))