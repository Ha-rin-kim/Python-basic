#한 개의 정수를 입력받아 양수(positive integer)인지 음수(negative number)인지
#출력하는 작업을 반복하다가 0이 입력되면 종료하는 프로그램을 작성하시오.

#while 문의 조건식으로 종료 조건을 작성

#조건식에 들어갈 변수 초기화
정수 = 1
#사용자 입력이 0이 아닌 경우 반복
while 정수: #정수 != 0: 조건과 일치
    #사용자가 정수값 입력
    정수 = int(input('number? '))
    #입력한 값이 음수인지 양수인지 판단 
    if 정수 > 0 :
        print('양수')
    elif 정수 < 0 : #else를 사용하면 정수 <= 0 와 같은 조건이기때문에 사용할수없음
        print('음수')
