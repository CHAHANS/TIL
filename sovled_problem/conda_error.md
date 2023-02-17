# Anaconda in VScode errors

1. Anaconda 설치 후 VScode에서 찾지 못함
    1. 애러
        - VScode 에서 conda 입력시 찾지 못했다.
    2. 해결
        - conda 경로가 환경벼녀수에 등록되지 않았다.
        1. 내PC 우크릭 > 고급 시스템 설정
        2. 시스템 설정에서 > 환경변수 > 새로만들기
        3. 총 3개의 경로를 추가로 생성했다.
            - ~Anaconda3(내 Anaconda3가 설치된 경로)
            - ~Anaconda3\Livrary
            - ~Anaconda3\Scripts
---
2. create 과정에서 SSLError 발생
    1. ML을 만들고 싶었다.
        ```cmd
        conda create --name ML
        ```
    2. 애러
        - CondaSSLError: OpenSSL appears to be unavailable on this machine. OpenSSL is required to download and install packages.

    3. 원인
        - 통신애러
        - 방화벽
        - SSL 접속애러

    4. Try
        1. 가장 먼저 conda create에 SSL 인증이 없어지는 명령어를 쳐봤다.
        ```cmd
        conda config --set ssl_verify False
        conda config --set ssl_verify no
        ```
    5. Solved
        - 바로 적용이 안되서 재부팅하니 된다.
        - wsl 까는김에 재부팅하고 혹시 나 해서 해봤더니 됐다.
        - 바로 활성화
