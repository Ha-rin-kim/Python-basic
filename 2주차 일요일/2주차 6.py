#break 문 사용하기

'''
break : 반복문 안에서 사용할 수 있는 키워드로 가장 안쪽에있는 반복문을 강제로
빠져나가게 하는 기능이 있음
반복문이 없는 상태에서 break를 사용하면 Error 발생
반복문이 두겹으로 곂쳐있는 상태에서 break를 사용하면 가장 안쪽에있는 반복문만
빠져나가게됨
while
    while
        break
    break 사용 시 이쪽 라인으로 빠져나옴
continue : 가장 안쪽에 있는 반복문의 맨첫줄로 강제 이동하는 기능
while문에서 continue를 사용할 경우, 다시 while의 조건을 비교하는 코드로 이동

'''

cnt = 0
while True: #무한 반복문, 무한 루프 : 반복문의 조건이 항상 참
    cnt += 1
    #5의 배수인경우 밑에 문장이 실행되지 않도록 설정
    if cnt % 5 ==0: #not (cnt % 5)
        print('반복문의 맨첫줄로 이동', cnt)
        continue
    if cnt >= 100:
        print('프로그램을 강제종료')
        break
    print(cnt)

















