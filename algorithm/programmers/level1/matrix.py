def solution(arr1, arr2):   
    return [list(map(sum, zip(*t))) for t in zip(arr1, arr2)]


arr1 = [[1], [2]]
arr2 = [[3], [4]]
print(solution(arr1, arr2))

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2))