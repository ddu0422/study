"""
NxN 크기 정사각 격자
바구니에 옮김
바구니에 같은 인형이 있는 경우 터짐
주의) 터진 후 다시 터질 수 있음

인형이 없는 곳에서 크레인 작동 시 아무일도 일어나지 않음
크레인을 모두 작동시킨 후 터트러져 사라진 인형의 개수를 구하시오.

0은 빈 칸을 의미

== example ==
1, 5, 3, 5, 1, 2, 1, 4

4, 3, 1, 1, 3, 2, 4
"""


def solution(board, moves):
    answer = 0
    busket = []
    size = len(board)

    for move in moves:
        for i in range(size):
            doll = board[i][move - 1]
            if doll:                
                busket.append(doll)
                board[i][move - 1] = 0
                answer += remove_doll(busket)
                break

    return answer


def remove_doll(busket):
    if len(busket) >= 2 and busket[-2] == busket[-1]:
        for _ in range(2):
            busket.pop()
        return 2
    
    return 0
    


board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))