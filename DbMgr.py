# 디비 처리, 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql as my

class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버함수
    '''
    def db_init(self):
        self.conn = my.connect(
                        host='localhost',
                        user='username',
                        password='password',
                        db='pythonDB',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor )
                        
    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기 => 웹에서 검색
    def db_selectKeyword(self):
        # 커서 오픈
        # with => 닫기 처리를 자동으로 처리해준다 => I/O 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows
        
    def db_insertCrawlingData( self, title, price, area, contents, keyword ):
        with self.conn.cursor() as cursor:
            sql = '''
            INSERT INTO tbl_crawlingData
            (title, price, area, contents, keyword)
            VALUES ( %s,%s,%s,%s,%s );
            '''
            cursor.execute(sql, (title, price, area, contents, keyword) )
        self.conn.commit()

# 단독으로 수행시에만 작동 => 테스트코드를 삽입해서 사용
if __name__ == '__main__' :
    db = DBHelper() # 연결
    print( db.db_selectKeyword() )
    print( db.db_insertCrawlingData('1','2','3','4','5') )
    db.db_free()    # 해제