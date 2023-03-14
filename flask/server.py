from flask import Flask
from flask import request, redirect
import random

app = Flask(__name__)

#나중에 DB에 넣어봐야지
topics = [
    {'id':1, 'title':'html', 'body':'html is...'},
    {'id':2, 'title':'css', 'body':'html is...'},
    {'id':3, 'title':'javacript', 'body':'html is...'}
    ]

def template(contents, content, id=None):
    contextUI = ''
    if(id != None):
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
        '''
    return f'''<!DOCTYPE html>
    <html lang="en">
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
        </html>
            '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    
    return template(getContents(), '<h2>Welcom</h2>Hello, WEB')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id== topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)


# @app.route('/create/', methods=['GET', 'POST'])
# def create():
#     #method를 바꾸면
#     if request.method == 'GET':    
#         content = '''
#             <form action="/create/" method="POST">
#                 <p><input type="text" name="title" placeholder="title"></p>
#                 <p><textarea name="body" placeholder="body"></textarea></p>
#                 <p><input type="submit" value="create"</p>
#             </form>
#         '''
#         return template(getContents(), content)
#     elif request.method == 'POST':
#         global nextID
#         title = request.form['title']
#         body = request.form['body']
#         newTopic = {'id': nextID, 'title':title, 'body':body}
#         topics.append(newTopic)
#         url = 'read/'+str(nextID)+'/'
#         nextID = nextID+1
#         return redirect(url)



# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update():
#     title = ''
#     body = ''
#     for topic in topics:
#         if id== topic['id']:
#             title = topic['title']
#             body = topic['body']
#             break
#     content = f'''
#         <form action="/update/{id}" method="POST">
#             <p><input type="text" name="title" placeholder="title" value="{title}"></p>
#             <p><textarea name="body" placeholder="body">{body}</textarea></p>
#             <p><input type="submit" value="update"</p>
#         </form>
#     '''
#     return template(getContents(), content)



#음성파일 전송 테스트 ****
# @app.route('/')

#기본 5000번 prot지만 5001로변경할 수 있다. debug=True로 실시간
app.run(port=5001, debug=True)