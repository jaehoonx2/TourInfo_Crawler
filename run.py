# 인터파크 투어 사이트에서 여행지를 입력 후 검색 => 잠시 후 => 결과
# 로그인 시 PC 웹 사이트에서 처리가 어려울 경우 => 모바일 로그인 진입
# 모듈 가져오기
# pip/pip3 install selenium
from selenium import webdriver as wd

from selenium.webdriver.common.by import By
# 명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 사전에 필요한 정보를 로드 => 디비 혹은 쉘, 베치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')      # Windows
#driver = wd.Chrome(executable_path='./chromedriver')       # MAC
# 차후 => 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래 돌리면 => 임시파일들이 쌓인다!! => temp 파일 삭제

# 사이트 접속 (get)
driver.get(main_url)
# 검색창을 찾아서 검색어를 입력
# id : SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 수정할 경우 => send_keys를 이어 쓸 경우, 뒤에 내용이 붙어버림 => .clear() => send_keys('내용')
# 검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

# 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제
# 명시적 대기 => 특정 요소가 locate(발견될 때까지) 대기
try:
    element = WebDriverWait(driver, 10).until(
        # 지정한 한개 요소가 올라오면 wait 종료
        EC.presence_of_element_located( (By.CLASS_NAME, 'oTravelBox') )
    )
except Exception as e:
    print('오류 발생', e)
# 암묵적 대기 => DOM이 다 로드될 때까지 대기하고 먼저라도 로드되면 바로 진행
# 요소를 찾을 특정 시간 동안 DOM의 풀링을 지시. 예를 들어 10초 이내라도
# 발견되면 바로 진행
driver.implicitly_wait( 10 )
# 절대적 대기 => time.sleep(10) -> 클라우드 페어(DDoS 방어 솔루션)
# 더보기 눌러서 => 게시판 진입
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()