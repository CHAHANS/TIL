# 1일차 tutorial 일단 시작하기
## 설치/실행 테스트
- 페이지에서 많은 사람이 사용한다며 추천하는 18.14.2 LTS로 다운했다.
- vscode에 필요할거라 안내되는 체크박스는 클릭하고 설치했다.
- 불안하게 powershell에서 Package Microsoft. ~~~ : 현재 OS 버전 ~은 지원되는 버전 범위 ~에 속하지 않습니다가 엄청 난무한다. -> 파워쉘 끄고 그냥 재설치
- MS가이드: window wsl 에서 설치 [참고](https://learn.microsoft.com/ko-kr/windows/dev-environment/javascript/nodejs-on-windows)
    - index.js생성하고 간단한 `console.log('hi')`로 저장
    - powershell에서 폴더위치 맞추고 `node .\index.js`로 찍어보니 정상작동한다.

## npm이란?
- [NPM](https://www.npmjs.com/): Node Packege Manger
- install 명령어 `npm install ###`