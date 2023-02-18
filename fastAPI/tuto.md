# Fast-API tuto
FastAPI Tuto를 진행해보고, 서버사용법에 익숙해지고자 한다.
## 환경
- 네이버 클라우드 Server 
- Vscode

## 설치
- 설치 명령어
```bash
pip install fastapi[all] #전체
pip install fastapi #일부
```
- 일단 바로 애러:
(1) 1차 애러

`Command "python setup.py egg_info" failed with error code 1 in ~`
이유는 모르겠고 커맨드 입력
```
sudo -H pip3 install --upgrade --ignore-installed pip setuptools
```
바로 다른 애러
`ERROR: Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.` 
PyYAML을 삭제 후 다른버전으로 재설치할 때 생기는 오류라는데.. 
pyYAML을 무시하고 재설취 한 뒤 다시 다른걸 사용하면 된단다.
```
pip install --ignore-installed PyYAML
```
warring이 발생하는데 가상환경으로 관리하라고 경고한다..
setuptools 명령어를 입력 후 fastAPI누르지 동작은 하지만 경고는 뜬다..
- uvicorn서버로 작동하도록 설치
```
pip install uvicorn
```

## 한걸음
[First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
1. 기본 실행
- Main.py 생성 후 코드입력
```python
from fastapi import FastAPI #불러오기
app = FastAPI() #인스턴스 생성
@app.get("/")
async def root():
    return {"message": "Hello World"}
```
- run live sever
    - main.py파일에서 app을 reload한다는 뜻이다.
```
uvicorn main:app --reload
```

2. 내 server의 docs
- run server 이후 생성된 url 뒤에 `/docs`를 붙여 documentation을 확인
    - automatic interactive API documentation
- `/redoc`는 다른 형식의 Documentation을 제공 
    - alternative automatic documentation

3. Operation methods
- post : to create data
- get : to read data
- put : to update data
- delete : to delete data
```python

@app.get("/") #path
async def root():
    return {"message": "Hello World"}

```
## 기능들
- git에 들어가니 한국어로 된 docs를 제공하는걸 확인했다. [한국어DOCS](https://github.com/tiangolo/fastapi/tree/master/docs/ko/docs/tutorial)
- 내가 구현해본 것들 순서로 정리해보고자 한다.

