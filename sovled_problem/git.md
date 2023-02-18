### 잔디가 심어지지 않는 현상
- 개요: 맨날 커밋해서 오랜만에 잔디보러 갓더니 없는거여!
- 문제: git config user.email과 git계정에 setting의 email이 달라서 발생
- 해결(1): 잔디가 심어지게
    git config list로 확인 후 git config user.email `email주소`로 다시설정
- 해결(2) : rebase 하는 방법  블록참고
[참고](https://wellbell.tistory.com/43)git

## git 용량 확대..

## git push시 처음보는 메세지가 나왔다.
- Push시:
    처음보는 메세지창을 습관처럼 하단 다시뭍지 않음을 선택후 닫아버렸는데
    `Username for 'https://github.com':`라는 처음보는 문구가 나왔다
- 이유:
    git에 access하는 방법과 관련된 내용이었던 것이다
    id와 passward를 물어보게 되고, 좀 위험하더라도 저장하고 사용하는게 가능하다.
- 해결:
    github > setting > Personal access tokens > Tokens(classic) > Generate new token
    'repo'를 기간은 '90일'을 선택하고 토큰을 발급았다.
    새로운 토근은 pw로 사용된다. push시 id는 내 이름을 pw는 생성된 토큰을 입력하면 해결된다.
    나는 매번 입력해야하고 토큰은 복사해서 잘 숨겨두었다.
    