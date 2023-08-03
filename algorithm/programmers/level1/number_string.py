"""
일부 자릿수를 영단어로 바꿈
=> 원래 숫자를 찾아야 함.

== example ==
1478 -> one4seveneight
"""
def solution(s: str):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for index, value in enumerate(numbers):
        s = s.replace(value, str(index))
        
    return int(s)

s = "23four5six7"
print(solution(s))