"""
양수, +, - 로 식을 만들었다.
적절히 괄호를 쳐서 값을 최소로 만드시오.

0-9, +, -

- 가장 처음과 마지막 문자는 숫자이다.
- 두 개 이상의 연산자가 나타나지 않는다.
- 수는 0으로 시작할 수 있다.
"""
text = input()


def solution(text):
    # -뒤에 나오는 숫자에 괄호를 치면 된다.
    text = text.split('-')
    answer = sum(map(int, text[0].split('+')))
    
    for value in text[1:]:
        answer -= sum(map(int, value.split('+')))

    return answer


print(solution(text))
