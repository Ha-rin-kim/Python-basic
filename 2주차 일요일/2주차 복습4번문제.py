#실수형 값을 입력받아 소수점이하 값이 없으면 "정수", 아니면 "실수"를 출력하는 프로그램

#실수값 입력
값 = float( input('값 입력 : ') )
#조건문을 이용한 정수/실수 구분
if 값 == int(값):#정수인 경우
    print("정수")
else:
    print("실수")
