"""
국회의원 후보: N
마을의 주민: M

다솜이 기호 1번
1번이 아닌 경우 돈으로 매수하여 1번을 찍도록 진행
매수해야하는 사람의 최솟값

"""
n = int(input())
votes =  [int(input()) for _ in range(n)]


def solution(votes):
    answer = 0
    dasom = votes[0]
    candidate = votes[1:] or [0]

    while dasom <= max(candidate):
        max_index = 0
        
        for index, value in enumerate(candidate):
            if candidate[max_index] < value:
                max_index = index

        candidate[max_index] -= 1
        dasom += 1
        answer += 1
    
    return answer


print(solution(votes))
