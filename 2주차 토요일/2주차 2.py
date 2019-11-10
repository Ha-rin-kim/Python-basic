#숫자/문자열/불 자료형으로 어떤값이 저장되있는지에 따라 True,False를 반환함

#if 조건문:
#if 변수나 상수값, 연산결과:
#숫자형 : 0일때 False, 0이 아닐 때 True
#ex) if 5: -> 항상 if문을 만족, if a -> a변수가 가진 값이 0이 아니면 if문을 만족

#문자열 : 아무 글자도 저장하지않을때 False, 한글자 이상을 저장할 때 True

#불 : True -> True, False -> False
'''
#정수 값을 if문에 넣었을 경우
a = int( input() )
if a:
    print("if문 만족")
#if a % 2 == 1: #홀수 판별
if a % 2: # a % 2 !=(같지않다) 0 
    print("홀수 판정")
'''
'''
#문자열을 if문에 넣었을 경우
a = input()
#len() : 문자열 길이 측정 함수
#len(a) : a가 가진 문자열의 길이를 반환함
if len(a) > 0: #a:
    print('if문 만족')
print("프로그램 종료")
'''
#불자료형을 if문에 넣었을 경우
a = True
b = False
#비교연산자의 결과 : True 또는 False
b = 5>3
if a:
    print("a조건 만족")

if b:
    print("b조건 만족")















