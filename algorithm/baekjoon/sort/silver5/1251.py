import sys

text = sys.stdin.readline().rstrip()


def solution(text):
    answer = []

    for i in range(1, len(text)):
        for j in range(i + 1, len(text)):
            answer.append(text[0:i][::-1] + text[i:j][::-1] + text[j:len(text)][::-1])

    return sorted(answer)[0]


print(solution(text))
