'''
2행 4열의 배열 두 개를 만들어서 입력을 받고
두 배열의 곱을 구하여 출력하는 프로그램을 작성하시오.
'''
#2행 4열짜리 리스트 변수 생성
리스트1 = [  [0,0,0,0], [0,0,0,0]  ]
리스트2 = [  [0,0,0,0], [0,0,0,0]  ]#[ [0] * 4 ] * 2
#입력 - 첫번째 리스트 변수
행 = 0
열 = 0
#행 반복 0~1
print('first array')
while 행 < 2: #행 <=1:
    #열 반복 0~3
    열 = 0  #반복문에 사용하기전 초기화
    while 열 < 4: #열<=3:
        #사용자 입력값을 행,열 인덱스에 저장
        리스트1[행][열] = int(input())
        열 += 1
    행 += 1
print('second array')
#입력 - 두번째 리스트 변수
행 = 0
while 행 < 2: #행 <=1:
    #열 반복 0~3
    열 = 0  #반복문에 사용하기전 초기화
    while 열 < 4: #열<=3:
        #사용자 입력값을 행,열 인덱스에 저장
        리스트2[행][열] = int(input())
        열 += 1
    행 += 1
#연산
행 = 0
while 행 < 2: #행 <=1:
    #열 반복 0~3
    열 = 0  #반복문에 사용하기전 초기화
    while 열 < 4: #열<=3:
        #첫번째 리스트의 행,열에 있는 값 * 두번째 리스트의 행,열에 있는 값
        리스트1[행][열] *= 리스트2[행][열]
        열 += 1
    행 += 1
        

#출력
print(리스트1)
























