"""
바로 앞/뒤만 체육복을 빌려줄 수 있음
체육복을 최대한 많은 학생이 입도록 해야함

n: 전체 학생 수
lost: 체육복을 도난당한 학생 번호
reserve: 여벌의 체육복을 가져온 학생 번호

주의) 여벌 체육복을 가져온 학생이 도난당할 수 있음
"""

def solution(n, lost, reserve):
    array = ['O'] * (n + 1)
    array[0] = 'N'
    
    spare_student = set(reserve) - set(lost)
    lost_student = set(lost) - set(reserve)

    for number in spare_student:
        array[number] = 'S'

    for number in lost_student:
        array[number] = 'X'

    # 여벌 체육복을 가져온 학생이 도난
    for number in set(lost) & set(reserve):
        array[number] = 'O'

    # 양 옆 번호인 경우 나누어 줌
    for i in range(1, n):
        if (array[i], array[i + 1]) == ('S', 'X') or (array[i], array[i + 1]) == ('X', 'S'):
            array[i], array[i + 1] = 'O', 'O'

    # 전체에서 체육복을 나눔받지 못한 학생을 뺌
    return n - array.count('X')


n = 5
lost = [3]
reserve = [3, 5]
print(solution(n, lost, reserve))