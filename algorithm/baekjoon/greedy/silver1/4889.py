"""
여는 괄호와 닫는 괄호만 이루어진 문자열이 주어진다.
안정적인 문자열을 만들기 위한 최소 연산의 수를 구하시오.

안정적인 문자열이란?
1. 빈 문자열은 안정적이다.
2. S가 안정적이라면 {S}도 안정적인 문자열이다.
3. S와 T가 안정적이라면, ST도 안정적이다.

연산은 여는 괄호 => 닫는 괄호 / 닫는 괄호 => 여는 괄호
"""
import sys


def solution(line):
    if not line:
        return 0
    
    queue = []
    answer = 0

    for value in line:
        # 안정적인 괄호인 경우 남은 문자에서 뺀다.
        if queue and queue[-1] == '{' and value == '}':
            queue.pop()
            continue
        queue.append(value)

    # 남은 문자 중 문자가 동일한 경우 ({{ 혹은 }}인 경우) 1회 변경하여 안정적인 문자열로 변경한다.
    # 남은 문자 중 문자가 다른 경우 ()}{인 경우) 2회 변경하여 안정적인 문자열로 변경한다.
    for i in range(0, len(queue) - 1, 2):
        if queue[i] == queue[i + 1]:
            answer += 1
        else:
            answer += 2

    return answer


index = 1
for line in sys.stdin:
    if '-' in line:
        exit(0)
    print("{}. {}".format(index, solution(line.rstrip())), end="\n")
    index += 1
