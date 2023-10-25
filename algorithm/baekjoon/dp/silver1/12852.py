n = int(input())
d = [987654321] * (n + 1)


def solution(n, d):
    result = [0] * (n + 1)
    d[1] = 0

    for i in range(2, n + 1):
        min_value = n + 2

        if not i % 3 and d[i] > d[i // 3] + 1:
            d[i] = d[i // 3] + 1 
            min_value = i // 3

        if not i % 2 and d[i] > d[i // 2] + 1:
            d[i] = d[i // 2] + 1
            min_value = i // 2

        if d[i] > d[i - 1] + 1:
            d[i] = d[i - 1] + 1
            min_value = i - 1

        result[i] = min_value

    value = n
    ansewr = [n]

    while value:
        if result[value] == 0:
            break

        ansewr.append(result[value])
        value = result[value]

    return ansewr


answer = solution(n, d)
print(len(answer) - 1)
print(*answer, sep=' ')
