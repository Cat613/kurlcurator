from flask import Flask, render_template
from flask_restx import Api, Resource
from todo import Todo
from recipe import Recipe

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

api = Api(
    app,
    version='0.1',
    title="JustKode's API Server",
    description="JustKode's Todo API Server!",
    terms_url="/",
    contact="justkode@kakao.com",
    license="MIT"
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def web(path):
    return render_template('index.html')

api.add_namespace(Todo, '/todos')
api.add_namespace(Recipe, '/recipe')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port = 80)