#사용자로 부터 숫자값을 받아 연산을 한뒤 결과를 보여주는 프로그램

#숫자 값 두개를 입력 받아 변수에 저장
a = int(input('첫번째 숫자값 입력'))
b = int(input('두번째 숫자값 입력'))
#각 연산의 결과와 수식을 화면에 출력
result = '%d+%d=%d' % (a,b,a+b) #a+b=c
print(result)

#변수에 문자열 포멧팅 결과를 넣지않고 print함수에 바로 넣기
print('%d-%d=%d' % (a,b,a-b) )

#문자열 포멧팅을 저장한 변수로 print함수에서 %연산하기
form = '%d %s %d = %d' #a(연산자기호)b = 연산결과
print(form % (a, 'X', b, a*b )) #곱하기
print(form % (a, '/', b, a/b ))
print(form % (a, '^', b, a**b))



