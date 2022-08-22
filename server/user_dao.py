import pymysql, configparser

ppt = configparser.ConfigParser() ## 클래스 객체 생성

ppt.read('config.ini')

host = ppt['DB']['host']
id = ppt['DB']['id']
pw = ppt['DB']['pw']
Database = ppt['DB']['Database']

class RecipeDao:
    def __init__(self):
        pass
    
    def getRecipe(self):
        ret = {}
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = "select * from CLIENT_MAIN";
        curs.execute(sql)
        
        rows = curs.fetchall()
        for user in rows:
            temp = {'CLIENT_ID':user[0],'CLIENT_PW':user[1],'CLIENT_NICK':user[2],'CLIENT_SEX':user[3],'CLIENT_BIRTH':user[4],'CLIENT_HEIG':user[5],'CLIENT_WEIG':user[6],'FRIDGE_ID':user[7],'DIARY_ID':user[8],'NUTST_ID':user[9],'CLINET_ACTIV_ID':user[10] }
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insRecipe(self, CLIENT_ID,CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID):
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = '''insert into CLIENT_MAIN (CLIENT_ID,CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        curs.execute(sql,(CLIENT_ID,CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID))
        db.commit()
        db.close()
    
    def updRecipe(self, CLIENT_ID,CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID): 
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = "update CLIENT_MAIN set CLIENT_PW=%s,CLIENT_NICK=%s,CLIENT_SEX=%s,CLIENT_BIRTH=%s,CLIENT_HEIG=%s,CLIENT_WEIG=%s,FRIDGE_ID=%s,DIARY_ID=%s,NUTST_ID=%s,CLINET_ACTIV_ID=%s where CLIENT_ID=%s"
        curs.execute(sql,(CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID,CLIENT_ID))
        db.commit()
        db.close()

    def delRecipe(self, CLIENT_ID):
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = "delete from CLIENT_MAIN where RECIPE_ID=%s"
        curs.execute(sql,CLIENT_ID)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    #MyEmpDao().insEmp('aaa', 'bb', 'cc', 'dd')
    #MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    #MyEmpDao().delEmp('aaa')
    RecipeList = RecipeDao().getRecipe();
    print(RecipeList)