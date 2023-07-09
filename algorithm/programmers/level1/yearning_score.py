def solution(name, yearning, photo):
    answer = []
    
    # 점수 초기화
    score_board = {}
    
    for i in range(len(name)):
        score_board.update({name[i]: yearning[i]})
        
    # 문제풀이
    for data in photo:
        sum = 0
        for name in data:
            score = score_board.get(name)
            if score != None:
                sum += score
        answer.append(sum)
    
    # 정답
    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))