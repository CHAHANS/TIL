from flask import Flask
# page : https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello</p>"


app.run(port=5000, debug=True)