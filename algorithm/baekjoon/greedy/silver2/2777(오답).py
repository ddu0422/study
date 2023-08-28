import sys

t = int(sys.stdin.readline().rstrip())


def solution(number):
    if number < 10:
        return 1

    answer = 0
    index = 9
    while index > 1:
        if number % index != 0:
            index -= 1
            continue

        answer += 1
        number //= index

        if number == 1:
            return answer
    
    return -1


for _ in range(t):
    sys.stdout.write(str(solution(int(sys.stdin.readline().rstrip()))) + "\n")
