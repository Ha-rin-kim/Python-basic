'''
년도를 입력받아 윤년(leap year)인지 평년(common year)인지
판단하는 프로그램을 작성하시오.

400으로 나누어떨어지면 윤년이다.
또는 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다.
나머지는 모두 평년이다.
'''
#년도 입력
년도 = int(input())
#윤년, 평년을 판단하는 조건문 작성
if 년도 % 400 == 0 #or (년도 % 4 == 0 and 년도 % 100 != 0):
    print('leap year')
elif (년도 % 4 == 0 and 년도 % 100 != 0):
    print('leap year')
else:
    print('common year')
