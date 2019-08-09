# 인터파크 투어 사이트에서 여행지를 입력 후 검색 -> 잠시 후 -> 결과
# 로그인 시 PC 웹 사이트에서 처리가 어려울 경우 -> 모바일 로그인 진입
# 모듈 가져오기
# pip/pip3 install selenium
from selenium import webdriver as wd

# 사전에 필요한 정보를 로드 -> 디비 혹은 쉘, 베치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'

# 드라이버 로드
#driver = wd.Chrome(executable_path='chromedriver.exe')     # Windows
driver = wd.Chrome(executable_path='./chromedriver')   # MAC
# 차후 -> 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래 돌리면 -> 임시파일들이 쌓인다!! -> temp 파일 삭제

# 사이트 접속 (get)
driver.get(main_url)
# 검색창을 찾아서 검색어를 입력
# id : SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 검색 버튼 클릭
# 잠시 대기 -> 페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는
# 자제 -> 