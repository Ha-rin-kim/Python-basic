'''
구글에 검색 키워드를 입력 후 검색어와 관련된 이미지들을 하드디스크에 저장하는
프로그램
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#이미지 파일 다운받기위한 웹 요청
import urllib.request
import base64 #HTML파일에 이미지데이터가 포함되있는 경우를 처리하기위한 라이브러리

driver = webdriver.Chrome('chromedriver')
driver.get('http://www.google.com') #구글 메인 페이지로 이동

time.sleep(2)

#메인페이지에서 검색창 찾기
search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
search.send_keys('고양이')
search.send_keys(Keys.ENTER)

#검색 결과 창에서 '이미지' 버튼 클릭
time.sleep(3) #페이지가 완전히 로드될수 있도록 3초 대기
image_btn = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
image_btn.click()

#이미지를 추출 및 파일 저장
#이미지페이지에서 <div> 찾기
#XPath 에서 일정 규칙을 가지는 경로를 *처리해서 가져올수있음
divs = driver.find_elements_by_xpath('//*[@id="rg_s"]/div[*]')
for i, div in enumerate(divs):
    #div 태그내에 있는 이미지 데이터를 추출
    #div 태그내에 있는 <img>요소를 추출
    try:
        image = div.find_element_by_tag_name('img')
        #<img> 요소에 src 속성 값을 추출
        #(src 속성이 실제 이미지 데이터 or 이미지가 존재하는 웹주소)
        src = image.get_attribute('src')
        if 'jpeg' in src: #src 변수에 jpeg 문자열이 존재하는지 확인->src변수에 실제이미지데이터
            #이미지 데이터 중 데이터 설명부분을 제외하기 위해 ','를 찾음
            split_idx = src.find(',')
            src = src[split_idx+1 : ]#슬라이싱 : 특정 범위에있는 문자열/리스트를 추출
            #소스파일경로/images/image_횟수.jpg 파일을 쓰기모드로 접근
            f = open('./images/image_%s.jpg' % i ,'wb')

            #파일 데이터가 base64 형태로 되어있어 base64 라이브러리를 사용
            f.write( base64.b64decode( src) ) #실제파일 데이터를 저장
            f.close()
        else: #이미지를 다운받을 수 있는 웹주소
            #urllib.request.urlretrieve(다운받을수있는 웹주소, 저장할 파일경로) 
            urllib.request.urlretrieve(src, './images/image_%s.jpg' % i)
    except:
        print('img태그가 없음')
    time.sleep(1)





































