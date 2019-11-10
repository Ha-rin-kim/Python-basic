'''
1번은 개, 2번은 고양이, 3번은 병아리로 정하고 번호를 입력하면 번호에 해당하는 동물을 영어로 출력하는 프로그램을 작성하시오. 
해당 번호가 없으면 "I don't know."라고 출력한다.
개-dog
고양이-cat
병아리-chick​ 
'''

#정수 입력
number = int(input('Number? '))
#정수값에 따라 결과를 출력
if number == 1:
    result = "dog"
    #print("dog")
elif number == 2:
    result = "cat"
    #print("cat")
elif number == 3:
    result = "chick"
    #print("chick")
else:
    result ="I don't know."
    #print("I don't know.")

print(result)










