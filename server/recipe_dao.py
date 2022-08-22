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
        
        sql = "select * from MAP_RECIPE_IMAGE";
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'RECIPE_ID':e[0],'RECIPE_SN':e[1],'RECIPE_CONT':e[2],'IMAGE_FILE_NM':e[3] }
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insRecipe(self, RECIPE_ID, RECIPE_SN, RECIPE_CONT,IMAGE_FILE_NM):
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = '''insert into MAP_RECIPE_IMAGE (RECIPE_ID, RECIPE_SN, RECIPE_CONT, IMAGE_FILE_NM) values(%s,%s,%s,%s)'''
        curs.execute(sql,(RECIPE_ID, RECIPE_SN, RECIPE_CONT,IMAGE_FILE_NM))
        db.commit()
        db.close()
    
    def updRecipe(self, RECIPE_ID, RECIPE_SN, RECIPE_CONT,IMAGE_FILE_NM): 
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = "update MAP_RECIPE_IMAGE set RECIPE_CONT=%s, IMAGE_FILE_NM=%s where RECIPE_ID=%s and RECIPE_SN=%s"
        curs.execute(sql,(RECIPE_CONT,IMAGE_FILE_NM, RECIPE_ID, RECIPE_SN))
        db.commit()
        db.close()

    def delRecipe(self, RECIPE_ID):
        db = pymysql.connect(host=host, user=id, db=Database, password=pw, charset='utf8')
        curs = db.cursor()
        
        sql = "delete from MAP_RECIPE_IMAGE where RECIPE_ID=%s"
        curs.execute(sql,RECIPE_ID)
        db.commit()
        db.close()
 
if __name__ == '__main__':
    #MyEmpDao().insEmp('aaa', 'bb', 'cc', 'dd')
    #MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    #MyEmpDao().delEmp('aaa')
    RecipeList = RecipeDao().getRecipe();
    print(RecipeList)