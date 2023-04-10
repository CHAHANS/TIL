from flask import Flask
import requests as request
# page : https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello</p>"

#프로젝트 test
@app.route('/create', methods=['POST'])
def create():
    print(request.is_json)
    params = request.get_json()
    print(params['id'])
    return 'done'


app.run(port=5000, debug=True)