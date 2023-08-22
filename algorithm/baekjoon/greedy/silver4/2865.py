"""
n: 참가자 수
m: 음악 장르

심사위원은 각 장르에 대한 능력을 점수로 매긴다. (실수)
총 K명 본선 진출
각 참가자는 단 하나의 장르만 부를 수 있다.
- 한 사람이 여러 장르를 부를 수 없지만 여러 사람이 같은 장르를 부를 수 있다.

능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램을 작성하시오.

=== example ===
3 2 2
2 3.0 1 0.2 3 0.1
3 1.0 2 0.5 1 0.2

=> 참가자별 높은 점수를 구한 후 순서대로 올리면 된다.

"""
n, m, k = map(int, input().split())
genre = []
for _ in range(m):
    genre.append(list(input().split()))


def solution(n, genre, k):
    scores = [0] * (n + 1)

    for value in genre:
        for i in range(0, len(value), 2):
            number, score = value[i:i+2]
            scores[int(number)] = max(scores[int(number)], float(score))
    
    return round(sum(sorted(scores, reverse=True)[:k]), 1)


print(solution(n, genre, k))
