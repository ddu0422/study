def solution(cards1, cards2, goal):
    # 초기화
    i = 0
    j = 0
    k = 0

    # 문제 풀이
    while True:
        # 종료 조건 1: Goal 완성 시 종료
        if k >= len(goal):
            return "Yes"
        
        current = goal[k]

        # 종료 조건 2: goal에 해당하는 card가 없는 경우 종료
        if cards1[i] != current and cards2[j] != current:
            return "No"

        if i < len(cards1) - 1 and cards1[i] == current:
            i += 1

        if j < len(cards2) - 1 and cards2[j] == current:
            j += 1

        k += 1

cards1=["i", "drink", "water"]
cards2=["want", "to"]
goal=["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))

cards1=["i", "water", "drink"]
cards2=["want", "to"]
goal=["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))