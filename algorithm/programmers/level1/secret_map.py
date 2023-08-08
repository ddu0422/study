"""
n: 한 변의 길이 (정사각형)
각 칸: 공백 or #
두 장의 지도를 겹쳐서 얻을 수 있다.

지도1과 지도2에서 모두 공백인 부분 => 전체 지도에서도 공백
"""

# https://brownbears.tistory.com/467 (진수 변환)
# https://www.delftstack.com/ko/howto/python/python-leading-zeros/ (leading zero)

def solution(n, arr1, arr2):
    return [
        format(num1 | num2, 'b').rjust(n, '0').replace('1', '#').replace('0', ' ') 
        for num1, num2, in zip(arr1, arr2)
    ]


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))