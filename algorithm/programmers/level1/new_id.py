"""
규칙에 맞지 않는 아이디를 입력했을 때
=> 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천

1. 아이디 길이 3~15
2. 소문사, 숫자, 빼기, 밑줄, 맞침표
3. .는 처음과 끝에 사용 불가 / 연속 사용 불가


변환
1. 대문자 => 소문자
2. 허용된 문자를 제외하고 모든 문자 제거
3. . 2번 이상인 경우 .로 치환
4. .가 처음이나 끝에 위치하는 경우 제거
5. 빈 문자열 => a로 변경
6. 16자 이상인 경우 첫 15개 문자를 제외한 나머지 문자 제거 (제거 후 마침표가 있다면 제거)
7. 2자 이하인 경우 new_id의 마지막 문자를 길이가 3이될 때까지 반복
"""
import re

def solution(new_id: str):
    # 1번 조건
    new_id = new_id.lower()

    # 2번 조건
    new_id = re.sub(r'[^a-z0-9-_\.]', '', new_id)

    # 3번 조건
    new_id = re.sub(r'(\.){2,}', '.', new_id)

    # 4번 조건
    new_id = re.sub(r'^\.|\.$', '', new_id)

    # 5번 조건
    if len(new_id) == 0:
        new_id = 'a'

    # 6번 조건
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub(r'\.$', '', new_id)
    
    # 7번 조건
    if len(new_id) < 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    
    return new_id


new_id = "-_.~!@#$()[]"
print(solution(new_id))