"""
1. 일렬로 놓여진 N개의 버튼이 모두 불이 꺼진 상태로 있다.
2. 0 또는 1로 구성되어 있는 N자리 수가 적힌 쪽지가 있다.
3. 0: 꺼짐, 1: 켜짐
4. 누르는 경우 0 -> 1, 1 -> 0
5. 버튼을 누르면 그 버튼 뿐만이 아닌 오른쪽 두 개의 버튼도 같이 눌린다.

불이 꺼진 상태에서 버튼을 최소로 눌러서 쪽지와 똑같은 상태로 만들어야한다.

7
1010101

0000000
1110000
1001000
1010100
1010101

0
1
10 -> 11 / 10
11 -> 11
100 -> 111 / 100
101 -> 111 / 100 / 101
110 -> 111 / 110
111 -> 111
1000 -> 1110 / 1001 / 1000
1001 -> 1110 / 1001
1010 -> 1110 / 1000 / 1010
1011 -> 1110 / 1011
"""
import sys
n = int(sys.stdin.readline().rstrip())
lights = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(lights):
    answer = 0
    result = [0] * (len(lights) + 2)

    # 다르면 누르고 같으면 넘어가기
    for i in range(len(lights)):
        if result[i] == lights[i]:
            continue
        result[i] ^= 1
        result[i + 1] ^= 1
        result[i + 2] ^= 1
        answer += 1
    
    return answer


print(solution(lights))
