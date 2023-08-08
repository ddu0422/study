def solution(array, commands):
    return [sorted(array[start - 1:end])[index - 1] for start, end, index in commands]


array = [1, 5, 2, 6, 3, 7, 4]
commands = [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3]
]
print(solution(array, commands))