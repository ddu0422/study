n, l = map(int, input().split())
heights = list(map(int, input().split()))[:n]


def solution(l, heights):
    heights.sort()

    for height in heights:
        if l >= height:
            l += 1
    
    return l


print(solution(l, heights))