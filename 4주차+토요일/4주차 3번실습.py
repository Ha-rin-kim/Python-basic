'''
계산기 프로그램
피연산자 두개와 연산자를 입력받아 해당 연산을 수행하는 함수 호출 및 결과 출력

함수 : 특정 기능을 구현하는 코드를 모르더라도 입력에 대한 출력값을 얻을 수있는
형태.
함수를 호출하기 위해서는 호출지점 전에 함수가 정의되있어야함
함수 정의
def 함수명(매개변수(옵션) ):
    함수에 들어갈 코드
    return 함수가 출력할 값(옵션)
함수명과 변수명은 공용으로 사용하기 때문에 같은 이름을 사용하지않도록 주의해야함
'''
#함수 정의
def add(a,b):
    result = a+b
    return result #함수를 호출한 지점에 넘겨줄 값을 return 오른쪽에 작성
def sub(a,b):
    result = a-b
    return result
def mul(a,b):
    result = a*b
    return result
def div(a,b):
    result = a/b
    return result
값1 = float(input())
값2 = float(input())
연산자 = input()

if 연산자 =='+':
    결과 = add(값1, 값2)#add함수에 a=값1, b=값2 형태로 호출, 결과값을 결과변수에 저장
    pass #pass : 코드를 작성하지 않아도 프로그램이 정상동작할수있는 키워드
elif 연산자 =='-':
    #결과 = sub(값1,값2)
    #값을 대입할 매개변수를 지정
    #매개변수의 순서와 상관없이 값을 대입할 수 있음
    결과 = sub(b=값1, a=값2 )
elif 연산자 =='*':
    결과  = mul(값1,값2)
elif 연산자 =='/':
    결과 = div(값1,값2)
print('연산결과:',결과)






















