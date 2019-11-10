#정수 두개, 문자열 한개 입력 -> 연산기호를 확인후 연산결과 출력

#정수 두개, 문자열 한개 입력 받아 변수
a = int(input())
b = int(input())
c = input()
#연산기호에 맞게 연산을 수행
result = 0
if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
elif c == '/':
    result = a / b

#결과 출력
print(result)
