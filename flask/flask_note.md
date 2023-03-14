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
