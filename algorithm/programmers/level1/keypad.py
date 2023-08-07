"""
왼손 엄지손가락: *
오른손 엄지손가락: #

1) 엄지손가락은 상하좌우 방향으로만 이동 가능 (거리: 1)
2) 1, 4, 7은 왼손 엄지손가락 사용
3) 3, 6, 9는 오른손 엄지손가락 사용
4) 2, 5, 8, 0은 둘 중 가까운 더 가까운 엄지손가락 사용
  4-1) 거리가 같은 경우 주 손잡이 이용 

"""

def solution(numbers, hand):
    answer = ''
    phone = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_hand = '*'
    right_hand = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = number
        
        if number in [3, 6, 9]:
            answer += 'R'
            right_hand = number
        
        if number in [2, 5, 8, 0]:
            x, y = phone[number]
            xl, yl = phone[left_hand]
            xr, yr = phone[right_hand]

            left_distance = abs(xl - x) + abs(yl - y)
            right_distance = abs(xr - x) + abs(yr - y)

            if left_distance < right_distance:
                answer += 'L'
                left_hand = number
            elif left_distance > right_distance:
                answer += 'R'
                right_hand = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = number
                else:
                    answer += 'L'
                    left_hand = number

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))