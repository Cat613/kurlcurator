import pymysql, configparser

ppt = configparser.ConfigParser() ## 클래스 객체 생성

ppt.read('config.ini')

host = ppt['DB']['host']
id = ppt['DB']['id']
pw = ppt['DB']['pw']
db = ppt['DB']['Database']

db = pymysql.connect(host=host, user=id, db=db, password=pw, charset='utf8')
curs = db.cursor()
 
 

sql = "select * from MAP_RECIPE_IMAGE";

insert_sql = '''insert into sample (column01, column02, column03) values ('aa','bb','cc')
'''

update_sql = '''
update sample set column01 = 'cc', column02 = 'bb'
where column01 = 'aa';
'''

delete_sql = '''
delete from sample 
where column01 = 'cc'
'''

def execute_query(sql):

    curs.execute(sql)
    
    rows = curs.fetchall()
    print(rows)
    
    db.commit()
    db.close()