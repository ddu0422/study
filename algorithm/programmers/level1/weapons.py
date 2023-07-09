def solution(number, limit, power):
    knights = [countDivisor(i) for i in range(1, number + 1)]

    return sum([knight if knight <= limit else power for knight in knights])

def countDivisor(number):
    count = 0
    
    for j in range(1, int(number**(1/2)) + 1):
        if number % j == 0:
            if j * j == number:
                count += 1
            else:
                count += 2

    return count
    

number = 10
limit = 3
power = 2

print(solution(number, limit, power))
