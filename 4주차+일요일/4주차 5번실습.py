p = open('test.txt') #기본 파일접근 방식이 read모드이므로 생략가능
'''
#한줄씩 파일 데이터를 읽는 방법
while True:
    
    data = p.readline()
    if data == "": #파일을 전부 읽은 경우 data변수에 빈문자열이 저장됨
        break
    print(data)
'''
'''
#파일 전체를 한꺼번에 읽어 줄단위로 리스트의 요소 추가
datas = p.readlines()
for data in datas: #리스트의 요소를 한개씩 추출해 data변수에 대입
    print(data,end='')#출력할 문자열 끝에 추가할 문자열을 end매개변수가 저장(기본값:줄바꿈)
print(datas)
'''
#파일 전체 데이터를 하나의 문자열로 처리
data = p.read()
print(data)
p.close()



















