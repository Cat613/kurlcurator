from flask import request
from flask import render_template
from flask_restx import Resource, Api, Namespace
from user_dao import UserDao
import json


User = Namespace(
    name="user",
    description="user API.",
)

@User.route('/api')
class GetRecipe(Resource):
    def user():
        li = UserDao().getUser()
        res = json.dumps(li, ensure_ascii=False, indent=4).encode('utf8')

        print(res)

        return render_template("signup.html", userList=li)

    def get(self):
        """user 목록을 가져옵니다."""
        
        li = UserDao().getUser()
        res = json.dumps(li, ensure_ascii=False, indent=4).encode('utf8')

        print(res)

        #return render_template("signup.html", userList=li)
        return render_template("index.html", userList=li)
    

    def post(self):
        """user 추가합니다."""
        CLIENT_ID = request.json.get('ID')
        CLIENT_PW = request.json.get('PW')
        CLIENT_NICK = request.json.get('nick')
        CLIENT_SEX = request.json.get('sex')
        CLIENT_BIRTH = request.json.get('birth')
        CLIENT_HEIG = request.json.get('hei')
        CLIENT_WEIG = request.json.get('wei')
        FRIDGE_ID = "fredge0001"
        DIARY_ID = "diary0001"
        NUTST_ID = "nutst0001"
        CLINET_ACTIV_ID = "cli0001"

        UserDao().insUser(CLIENT_ID,CLIENT_PW,CLIENT_NICK,CLIENT_SEX,CLIENT_BIRTH,CLIENT_HEIG,CLIENT_WEIG,FRIDGE_ID,DIARY_ID,NUTST_ID,CLINET_ACTIV_ID)
        return {
            "insert" : "success"
        }

