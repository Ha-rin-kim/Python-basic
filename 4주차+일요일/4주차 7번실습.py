'''
pickle 외장 라이브러리
: 변수가 저장한 다양한 자료형(숫자,문자열,리스트,튜플,딕셔너리) 자체를
파일에 저장하는 기능을 제공하는 라이브러리
'''
import pickle
#문자열이 아닌 값을 파일에 저장할 때, 바이너리(b)모드를 추가해야함
파일 = open('data.bin', "wb")
data ={ '이름':'홍길동', '나이' : 25 , '성적' : 50 }
pickle.dump(data, 파일) #해당하는 파일에 변수에 저장된 값을 저장
a = [1,2,3,4,5,7,7,{1:2,3:5},3,4,3]
pickle.dump(a, 파일)
파일.close()

파일 = open('data.bin', 'rb')
other = pickle.load(파일) #열려있는 파일에 데이터를 불러오기
print(other)
other = pickle.load(파일)
print(other)
파일.close()





















