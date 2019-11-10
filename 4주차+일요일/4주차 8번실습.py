'''
유튜브 동영상 검색 프로그램
웹 크롤링 : 웹에 정보를 가져오는 일련의 과정
HTML : 인터넷 브라우저를 통해 그래픽으로 변환할 텍스트기반의 언어
XPath : 현재 HTML 페이지에서 선택하고자하는 요소의 경로값
'''
#selenium으로 원격조종하는 상태에서 특수키입력 처리
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #크롬 웹을 조종할 때 사용하는 라이브러리
import time #시간과 관련된 함수가 있는 라이브러리

#검색 키워드를 사용자입력으로 처리
검색어 = input('유튜브 검색 키워드 입력 : ')




#크롬드라이버를 로드
driver = webdriver.Chrome('chromedriver')
#get 함수로 인터넷 창 로드
driver.get("http://www.youtube.com/")
검색창 = '//*[@id="search"]'
#유튜브 사이트가 완전히 열릴때까지 대기
time.sleep(3) #time.sleep(대기할시간 초단위)

#전체 HTML파일 중에서 검책창을 찾기
#find_element_by_xpath(xpath 문자열) : 열려있는 페이지에서 XPath가 동일한 요소를 추출
#추출한 값을 저장한 변수를 활용해 텍스트입력 or 클릭
search = driver.find_element_by_xpath(검색창)
#검색창에 검색어 입력
search.send_keys(검색어)
search.send_keys(Keys.ENTER)
time.sleep(3)
#검색결과 중 키워드를 포함하고 있는 영상을 클릭
#find_elements_by_xpath : 입력으로 사용한 XPath와 동일한 요소 모두가져오기(리스트타입반환)
목록들 = driver.find_elements_by_xpath('//*[@id="video-title"]')
for 목록 in 목록들 :
    동영상제목 = 목록.text #요소가 가지고있는 글자 추출
    #요소 in 문자열/리스트/튜플 -> 해당 요소가 문자열/리스트/튜플에 존재하는지 T/F 연산
    print(동영상제목)
    #검색 키워드가 포함된 제목을 가졌는지 확인
    if 검색어 in 동영상제목:
        목록.click() #해당 요소(동영상제목)을 클릭하는 함수
        break






























