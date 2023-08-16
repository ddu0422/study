"""
동전의 양면에는 절대값이 같고 부호가 다른 정수가 한 면에 하나씩 쓰여있다.
(동전끼리는 쓰인 수의 절댓값이 다를 수 있다. = 같을 수 있다.)

2번의 라운드 = 같은 동전으로 진행
N개의 동전 = 섞은 후 일렬로 배열 (앞뒤 방향 바뀔 수 있음.)

1라운드 - 최대가 되도록 뒤집기
2라운드 - 최소가 되도록 뒤집기

연속한 3개의 동전만 뒤집기
(동전 끝의 동전만 뒤집는 경우 가능 1개, 2개)
=> 동전을 뒤집는 횟수는 제한이 없다.
"""
n = int(input())
round1 = list(map(int, input().split()))[:n]
round2 = list(map(int, input().split()))[:n]


def solution(round):
    # 동전을 끝에서부터 1개, 2개로 뒤집을 수 있기 때문에 몇 개가 오던 상관없이 모두 +로 변경할 수 있다.
    # => -가 붙은 동전이 3n번째에 위치하는 경우 => 3n - 1까지 뒤집을 수 있다.
    # 모두 +로(최대) 변경이 가능하다는 의미는 모두 -(최소)로 바꿀 수 있다는 걸 의미한다.
    # 최대든 최소든 양 면으로 동일한 값이 때문에 하나의 함수에소 최대는 + 최소는 -를 붙여 사용하면 된다.
    return sum([abs(value) for value in round])

print(solution(round1) * 2)