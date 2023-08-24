"""
해결한 경우 파란색
해결하지 못한 경우 빨간색

1. 연속된 임의의 문제들을 선택
2. 선택된 문제들을 전부 같은 색으로 칠한다.

=== example ===
1-2 파
3   빨
4   파
5   빨
6-7 파
8   빨

=> 6번 수행
1-7 파
3   빨
5   빨
8   빨

=> 4번 수행

최소 작업 횟수는?
"""
import re

n = int(input())
text = input()


def solution(text):
    # 연속으로 나온 문자는 하나의 문자로 변경한다.
    for value in ['B', 'R']:
        standard = '(' + value + '){2,}'
        text = re.sub(r'{}'.format(standard), value, text)
    
    # 둘 중 많은 색으로 칠하기(1) + 나머지 칠하기
    return 1 + min(text.count('B'), text.count('R'))


print(solution(text))



def solution_refactor(text):
    # 연속된 문자열은 하나의 원소로 이루어진다.
    r = text.split('B')
    b = text.split('R')
    
    return 1 + min(len(r) - r.count(''), len(b) - b.count(''))


print(solution_refactor(text))