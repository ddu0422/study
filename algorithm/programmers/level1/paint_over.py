def solution(n, m, section):
    if m == 1:
        return len(section)
    
    # 초기화
    result = 0

    array = [False] * (n)
    for i in section:
        array[i - 1] = True

    # 문제 풀이
    index = 0

    while index < n:
        if array[index]:
            result += 1
            index += m
        else:
            index += 1
            
    return result
    


n = 8
m = 4
section = [2, 3, 6]

print(solution(n, m ,section))

n = 5
m = 4
section = [1, 3]

print(solution(n, m ,section))

n = 4
m = 1
section = [1, 2, 3, 4]

print(solution(n, m ,section))