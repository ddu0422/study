from copy import deepcopy

# solution 1
# O(n^2)
def solution1(players, callings):    
    for calling in callings:
        current = players.index(calling)
        players[current - 1], players[current] = players[current], players[current - 1]
    
    return players

# solution 2
# O(n)으로 변경하기
def solution2(players, callings):
    # 초기화
    players_map = {}

    for (index, value) in enumerate(players):
        players_map.update({value: index})  

    # 문제풀이
    for calling in callings:
        # 현재 순위 가져오기
        index = players_map[calling]
        front_name = players[index - 1]

        # 역전 이름 변경
        players[index], players[index - 1] = players[index - 1], players[index]

        # 현재 순위 변경
        players_map[calling] = index - 1
        players_map[front_name] = index

    players_map = sorted(players_map.items(), key=lambda x: x[1])

    # 정답 구하기
    answer = [key for (key, _) in players_map]

    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution2(players, callings))