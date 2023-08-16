text = input()


def solution(text):
    ucpc = 'UCPC'
    index = 0
    
    for alpha in text:
        if ucpc[index] == alpha:
            index += 1

        if index == 4:
            break
    
    return 'I love UCPC' if index == 4 else 'I hate UCPC'


print(solution(text))
