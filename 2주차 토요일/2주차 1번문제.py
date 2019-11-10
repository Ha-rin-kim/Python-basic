#복싱체급은 몸무게가 50.80kg 이하를 Flyweight 61.23kg 이하를 Lightweight,
#72.57kg 이하를 Middleweight, 88.45kg 이하를 Cruiserweight,
#88.45kg 초과를 Heavyweight라고 하자.
#몸무게를 입력받아 체급을 출력하는 프로그램을 작성하시오.

#몸무게 입력(실수형)
몸무게 = float( input('몸무게 입력 : ') )
#조건을 만족하는 체급을 출력
#if ~ elif ~ else 문을 활용
'''
if 몸무게 <= 50.8:
    print("Flyweight")
elif 몸무게 <= 61.23:
    print("Lightweight")
elif 몸무게 <= 72.57:
    print('Middleweight')
elif 몸무게 <= 88.45:
    print('Cruiserweight')
else:    #elif 몸무게 > 88.45:
    print('Heavyweight')
'''    
#if 문만 활용
if 몸무게 <= 50.8:
    print("Flyweight")
if 50.8 < 몸무게 <= 61.23:
    print("Lightweight")
if 61.23 < 몸무게 <= 72.57:
    print('Middleweight')
if 72.57 < 몸무게 <= 88.45:
    print('Cruiserweight')
if 몸무게 > 88.45:
    print('Heavyweight')











