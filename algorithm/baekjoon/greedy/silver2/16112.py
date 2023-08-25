"""
n개의 아케인스톤 / 개당 5억
i번째 퀘스트를 진행하면 ai의 경험치와 i번째 아케인스톤이 주어집니다.
보상 경험치를 받을 때 ai의 경험치가 추가됩니다.

최대 경험치 제한을 없앰.
k개의 아케인스톤이 동시에 활성화될 수 있도록 변경

=== example ===
2번째 퀘스트를 진행해 100,000 경험치 주어진 경우
1, 3번째 아케인스톤에 100,000 경험치가 추가
2번째 아케인스톤 획득 경험치: 0

3 2
100 300 200

첫 번째 퀘스트를 진행하고 첫 번째 아케인스톤을 받은 뒤 활성화
0

세 번째 퀘스트를 진행하고 세 번째 아케인스톤을 받은 뒤 활성화
200 0

두 번째 퀘스트를 진행하고 두 번째 아케인스톤을 받은 뒤 활성화
500 300
"""
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
stones = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(stones, k):
    answer = 0
    count = 0

    for stone in sorted(stones):
        answer += count * stone
        if count < k:
            count += 1
    
    return answer


print(solution(stones, k))
