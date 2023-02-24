# Docker 설치
 - 윈도우 10, vscode, WSL:Ubuntu
1. 설치
    ```
    curl -sSL get.docker.com|sh 
    docerk --version
    ```
2. wheel 그룹 

    ```
    grep -E 'sudo|whell' /etc/group
    ```
* 옵션 -E, --estended-regexp
    
    PATTERNS are extended regular expressions

    ```
    usermod -aG sudo $USER
    ```
* 애러발생: $USER가 아닌 내 userid(hansol)를 입력했더니 애러남

    usermod: Premission denied.

    usermod: cannot lock /etc/passwd; try agrain later

    권한이 없는건가 싶어
    ```
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    ```
    입력 후 해결된것 처럼 보임. 다시 usermod 적용시 애러는 나지 않음.
    그러나 그냥 $USER로 쓰면 애러 날 이유가 없다.

- usermod는 사용자계정관리를 위해 사용(신입사원/계약직)
- wheel grop은 sudo, su를 위한 것

3. 경로에 ip입력
    ```
    sudo usermod -aG sudo $USER
    sudo usermod -aG docker $USER
    ```
    ```
    echo '' >> ~/.profile
    echo '# set DOCKER_HOST for docker default context' >> ~/.profile
    echo 'wsl_ip=$(ip addr show eth0|grep -oP "(?<=inet\s)\d+(\d+){3}")' >> ~/.profile
    echo 'export DOCKER_HOST=tcp://$wsl_ip:2375' >> ~/.profile
    ```

4. 실행
    (1) 첫 실행
    ```
    sudo service docker start
    sudo docker pull ubuntu:20.04
    sudo docker run -it --name test-ubuntu ubuntu:20.40 /bin/bash
    sudo docker run --name test-ubuntu2 ubuntu:20.40
    ```
    - --name 뒤에 이름을 바꿔서 실행하면 새로 생긴다.
    - run은 (생성+실행), -it(생성후 접속), 생성: create, 시작은 start 
    - wsl 1에서 작동이 안되는 경우가 많은듯 하다.

    (2) 상태 확인
    ```
    sudo service docker status
    ```
    ```
    sudo docker images
    ```
    ```
    sudo docker ps -a
    ```
    - 실행중인 container를 모두 보여줌

    (3) 접속
    ```
    sudo docker attach <CONTAINER NAME/ID>s
    ```
    (4) 실행
    ```
    sudo docker start <CONTINER NAME/ID>
    ```
    (5) 생성
    ```
    sudo docker create ~~
    ```

5. 메세지 주고받아보기
    ```
    sudo service docker start
    ```
    1. 메인터미널(서버)
        
        ```
        sudo docker start <name>
        sudo docker attach <name>
        apt-get update
        apt-get install python3
        ```
        ```
        #ip 확인, python 실행
        ipconfig
        python3
        ```
        ```python
        from socket import *
        svrsock =socket(AF_INET, SOCK_DGRAM)
        svrsock.bind('<IP주소>', 5000) #포트를 열고 대기
        ```
        ```python
        #메세지 받기: 1024는 저장될 공간
        msg, addr = svrsock.recvfrom(1024)
        print(msg)
        print(addr) #클라리언트가 지정하지 않고 생성된 랜덤 포트를 확인할 수 있다.
        #한글을 받을 때 decode 필요
        msg.decode()
        ```
        ```python
        #메세지 응답
        svrsock.sendto('<응답메세지>'.encode, addr)
        ```
    2. 추가터미널(클라이언트)
        ```
        sudo docker start <name2>
        sudo docker attach <name2>
        apt-get update
        apt-get install python3
        ```
        ```
        #ip 확인, python 실행
        ipconfig
        python3
        ```
        ```python
        from socket import *
        svrsock =socket(AF_INET, SOCK_DGRAM)
        svrsock.sendto('<내가보낼 메시지>'.encode()), ('<IP주소>', 5000)
        ```
        ```python
        #응답받기 
        msg, addr = svrsock.recvfrom(1024)
        msg.decode()
        ```


*컨테이런란?
 - 실행을 위해 필요한 모든 요소를 포하함 소프트웨어 패키지
 - 운영체제를 가상화
 - 데이터센터, 클라우드, 노트북, 데스크 탑 어디에서나 실행이된다.
 예) 컴퓨터환경에서 개발된 코드를 내 노트북에서도 되게끔
 - 컨테이너 이전에는 Virtual Machine을 사용하고, 자원까지 가상화했다. 차이점을 보고싶다면 [참고](https://www.netapp.com/blog/containers-vs-vms/)

# Docker를 이용해서 Linux 익숙해지기
- docker를 이용해 ubuntu container를 다운로드

- nslookup 설치
- sudo apt-get install dnsutils
명령어나 개념을 추가로 정리할 필요가 있다.

