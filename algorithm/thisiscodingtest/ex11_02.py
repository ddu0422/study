"""
입력
02984

출력
576

입력
567

출력
210
"""
str = input()
result = 0

for s in str:
  number = int(s)

  if number <= 1 or result <= 1:
    result += number
  else:
    result *= number

print(result)