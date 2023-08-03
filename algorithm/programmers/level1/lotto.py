"""
1: 6개 번호 일치
2: 5개 번호 일치
3: 4개 번호 일치
4: 3개 번호 일치
5: 2개 번호 일치
6: 0,1개 번호 일치

로또에 낙서
=> 알아볼 수 없는 번호 0

== example ==
구매번호: 44, 1, 0, 0, 31, 25
당첨번호: 31, 10, 45, 1, 6, 19

최고순위: 0 -> 10, 0 -> 6: 4개번호 일치 (3등)
최저순위:                  2개번호 일치 (5등)

최고 순위와 최저 순위 반환:  [3, 5]

최고 순위를 구하는 경우
- 0을 모두 일치하는 번호로 생각하여 진행

최저 순위를 구하는 경우
- 0을 모두 일치하지 않는 번호로 생각하여 진행

최저 순위를 구한 후 0의 개수만큼 더하기
"""

def solution(lottos, win_nums):
    prize = [-1, 6, 5, 4, 3, 2, 1, 0]
    
    minimum = len(set(lottos) & set(win_nums))
    maxmimum = min(6, minimum + lottos.count(0))

    return [min(6, prize.index(maxmimum)), min(6, prize.index(minimum))]


lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]
print(solution(lottos, win_nums))