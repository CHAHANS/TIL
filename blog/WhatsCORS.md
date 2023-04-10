# CORS란 ?

## 배경
- flask로 ML서버를 만들고, web은 django, view.js로 개발중이었다.
- view.js 로 요청했을 때 flask 서버에서 OPTIONS로 신호를 받아서 왜그런지 찾고자 했다.

## django와 view.js는 AJAX요청을 사용한다 ?
- 그럼 ajax는 뭘까

## CORS 정책때문이다?