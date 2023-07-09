"""
럭티 스트레이트 => 특정 조건

특정 조건:
현재 캐릭터 점수 N

1. N을 반으로 나눔
2. 왼쪽 부분의 각 자릿수의 합 == 오른쪽 부분의 각 자릿수의 합
3. 항상 짝수 형태로만 들어옴
4. 럭키 스트레이트 O => LUCKY, X => READY
"""
score = input()
length = len(score) // 2
left = sum(map(int, score[:length]))
right = sum(map(int, score[length:]))

print("LUCKY" if left == right else "READY")