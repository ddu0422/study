def solution(n):    
    measure = [0]

    for i in range(1, int(n**(1/2) + 1)):
        if n % i == 0:
            measure.append(i)
            measure.append(n // i)

    return sum(set(measure))


n = 1
print(solution(n))
