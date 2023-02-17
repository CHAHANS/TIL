### 잔디가 심어지지 않는 현상
- 개요: 맨날 커밋해서 오랜만에 잔디보러 갓더니 없는거여!
- 문제: git config user.email과 git계정에 setting의 email이 달라서 발생
- 해결(1): 잔디가 심어지게
    git config list로 확인 후 git config user.email `email주소`로 다시설정
- 해결(2) : rebase 하는 방법  블록참고
[참고](https://wellbell.tistory.com/43)git

## git 용량 확대..