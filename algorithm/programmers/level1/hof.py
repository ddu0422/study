import heapq


def solution(k, score):
    answer = []
    hof = []

    for number in score:
        # 최소힙이므로 자동 정렬되어 들어간다.
        heapq.heappush(hof, number)

        # 기준보다 많은 경우 최솟값을 제외한다.
        if len(hof) > k:
            heapq.heappop(hof)

        # 가장 처음은 최솟값이므로 결과값을 넣는다.
        answer.append(hof[0])

    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))