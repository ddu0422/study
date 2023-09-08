import sys

n = int(sys.stdin.readline().rstrip())
people = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    people.append([int(age), name, i])


def solution(people):
    return sorted(people, key=lambda x: (x[0], x[2]))


for age, name, _ in solution(people):
    print(age, name, end='\n')
