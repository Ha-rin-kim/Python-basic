'''
네이버의 얼굴인식 기능 사용하기
네이버 개발자 사이트에 기능 사용허가를 받은 뒤,
발급받은 ID, PASS로 요청
'''
import requests #웹사이트에 요청을 전달하는 라이브러리
import json     #파이썬의 사전형 데이터로 변환시켜주는 라이브러리

client_id = 'iZOXwOhrrnoXhvrhEM1W'
client_pass = 'LRm_9QRhI_'
url = "https://openapi.naver.com/v1/vision/face"

#웹사이트에게 전달할 이미지데이터 저장변수
#전달할 값들을 변수로 생성 - 인덱스 이름은 개발자사이트에서 확인해야함
files = {'image' : open('face1.jpg','rb')}
headers = {'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret':client_pass}
#웹사이트에게 데이터를 전달하면서 요청
#요청방식 GET/POST
response= requests.post(url, files=files, headers = headers)
#응답결과를 저장한 변수 response.text (문자열 타입)
print(response.text)
datas = json.loads(response.text) #문자열 -> 사전형
print(datas)
print('감지된 얼굴 수 :', datas['info']['faceCount'])
































