"""
AAAA와 BB 사용 가능
.와 X로 이루어진 보드판
X를 모두 AAAA / BB로 덮으려고 함 (단, .은 덮으면 안됨)

사전순으로 가장 앞서는 답 출력
주의) 덮을 수 없으면 -1 출력
"""


board = input()


def solution(board):
    board = board.split('.')
    result = []
    
    for element in board:
        count_x = element.count('X')
        if count_x % 2 != 0:
            return -1
        else:
            a = count_x // 4
            b = count_x % 4
            result.append('AAAA' * a + 'B' * b)

    return '.'.join(result)


print(solution(board))
