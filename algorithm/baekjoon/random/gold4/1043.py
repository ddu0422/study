import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())
knows = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
parties = []
parent = [i for i in range(n + 1)]

for know in knows:
    parent[know] = -1


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    people = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
    parties.append(people)

    for x, y in itertools.combinations(people, 2):
        union_parent(parent, x, y)


result = 0

for party in parties:
    know = False

    for person in party:
        if find_parent(parent, person) == -1:
            know = True
            break

    if not know:
        result += 1

print(result)
