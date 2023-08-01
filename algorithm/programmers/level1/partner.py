"""
짝궁: 두 수 X, Y의 임의의 자리에서 공통으로 나타나는 정수를 이용한 가장 큰 정수
예외 1) 짝궁이 존재하지 않으면 -1
예외 2) X, Y의 짝궁이 0으로만 구성되어 있다면, 짝궁은 0

== example ==
case 1)
X = 3403
Y = 13203

=> 공통 숫자 3, 0, 3
짝궁: 330

case2)
X = 5525
Y = 1255

=> 공통 숫자: 5, 2, 5
짝궁: 552

X에서 5는 3개 Y에서 5는 2개이므로, X에서 5 1개는 짝궁으로 사용할 수 없음.
"""

def solution(X, Y):
    numbersX = [0] * 10
    numbersY = [0] * 10

    for x in X:
        numbersX[int(x)] += 1

    for y in Y:
        numbersY[int(y)] += 1

    numbers = [min(numbersX[i], numbersY[i]) for i in range(10)]
    result = [str(number) * count for number, count in enumerate(numbers)]
    partner_numbers = ''.join(sorted(result, reverse=True))

    # 예외 1
    if not partner_numbers:
        return '-1'

    # 예외 2
    if partner_numbers.startswith('0'):
        return '0'
    
    return partner_numbers


X = "100"
Y = "2345000"

print(solution(X, Y))