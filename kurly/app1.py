from flask import Flask, render_template, session, url_for, redirect, request
from flask_restx import Api, Resource
from todo import Todo
from recipe import Recipe
from user import User
from user_dao import UserDao

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def web(path):
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
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
        
        return redirect(url_for('signup'))
    else:
        li = UserDao().getUser()
        return render_template('signup.html', userList=li)

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    empno = data['empno']
    name = data['name']
    department = data['department']
    phone = data['phone']
    cnt = MyEmpDao().insEmp(empno, name, department, phone)
    result = "success" if cnt==1 else "fail"
    return jsonify(result = result)

api.add_namespace(Todo, '/todos')
api.add_namespace(Recipe, '/recipe')
api.add_namespace(User, '/user')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port = 80)