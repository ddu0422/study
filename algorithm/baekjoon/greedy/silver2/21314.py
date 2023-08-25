"""
민겸 숫자: 0 이상의 정수 N에 대해 [10^N 또는 5 x 10^N] 꼴의 십진수 대문자 M과 K로 이루어진 문자열로 표기
10의 거듭제곱 or 10의 거듭제곱 * 5

1: M
5: K
10: MM
50: MK

505500: MKKMMK
변환될 수 있는 십진수 중 가장 큰 값과 가장 작은 값
"""
text = input()


def solution(text):
    max_value = ''
    min_value = ''
    count = 0

    for value in text:
        if value == 'M':
            count += 1
        else:
            if count > 0:
                min_value += str(10**(count - 1))
            min_value += '5'
            max_value += '5' + '0' * count
            count = 0
    
    if count > 0:
        min_value += str(10**(count - 1))

    return [max_value + '1' * count, min_value]


print(*solution(text), sep="\n")
