# Flask
[공식](https://flask.palletsprojects.com/en/2.2.x/)
### 개발환경
```
pip install flask
```


### 실행방법
- 2가지 방법으로 실행이 가능하다. 
- 명령어 종류에 따라 debug모드 등 사용할 때 조금 
1. Flask CLI 사용 [링크](https://flask.palletsprojects.com/en/2.2.x/cli/)
    - 실행 : $ flask --app <파일이름> run
    - 모든 공용  IP에서 수신 : $ flask run --host=0.0.0.0
2. python 실행형식
    - <파일이름>.py 파일 최 하단에 app.run()을 추가한다.
    - 실행 : $ python <파일이름>.py

### 조금 헷갈렸던 것들

```python
@app.route('/create/', methods=['GET', 'POST'])
def create():
    #method를 바꾸면
    if request.method == 'GET':    
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"</p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextID
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextID, 'title':title, 'body':body}
        topics.append(newTopic)
        url = 'read/'+str(nextID)+'/'
        nextID = nextID+1
        return redirect(url)
```
- form 태그를 사용해서 입출력을 하는과정이 헷갈렸던것 같다. input type이 submit인 경우 value 그리고 action으로 보내주는 부분에서 조금 허둥지둥 했다. w3school에서 해당 태그를 바꿔보면 2분만에 이해가 완료된다.
- 우선 GET과 POST를 명확하게 해야했는데, request.mothod로 조건을 건 것은 app.route에 url을 입력해서 접근하면 GET으로 POST방식으로 받아 접근하면 POST조건이 실행된다.