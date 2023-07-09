"""
입력: 알파벳 대문자 / 숫자 (0-9) 문자열
1. 알파벳을 오름차순으로 정렬
2. 모든 숫자를 더한 값을 이어서 출력
"""
data = input()
total = 0
result = ""

for datum in data:
  if datum.isdigit():
    total += int(datum)
  else:
    result += datum

result = sorted(result)

for s in result:
  print(s, end="")
print(total)