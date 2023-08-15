"""
대회 이름 정하기 규칙
1. 알파벳 대문자로 구성된 길이 N의 문자열 S를 정한다.
2. S에서 0개 이상의 문자를 지워서 대회 이름 T를 만든다.
3. T는 길이가 M인 운영진이 좋아하는 이름
- 맨 뒷글자는 알파벳 자음(AEIOU 제외) 
- 뒤에서부터 각각 두번째와 세번째 글자는 A인 문자열

최소 AAㅁ 가 되어야 함.
"""
import sys

n, m = map(int, input().split())
s = sys.stdin.readline().rstrip()


def solution(m, s):
    exclude = ['A', 'E', 'I', 'O', 'U']
    answer = ''
    i = 1

    for value in s:
        if i < m - 2:
            answer += value
            i += 1
        
        if i in [m - 2, m - 1] and value == 'A':
            answer += value
            i += 1     
        
        if i == m and value not in exclude:
            answer += value
            break
        
    return answer if len(answer) == m else ''


answer = solution(m, s)
if answer:
    print('YES')
    print(answer)
else:
    print('NO')
