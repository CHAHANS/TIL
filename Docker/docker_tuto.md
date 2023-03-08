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
6. 리눅스의 사용자와 권한
    - 디렉토리
        - /etc/passwd (계정설정)
        - /etc/shadow (계정암호화)
        - /etc/group  (사용자 그룹): `그룹명: 유저`
    - ctrl + d : logout

    1. 계정
        - 관리자 (root)#
        - 사용자 (user, username)$
    2. 그룹
        - 계정이 속해있는 그룹(없을수 없음)
    3. 생성
        ```
        useradd <username>
        adduser <username>
        passwd <PW>
        ```
        - 주의 : root에서 `su user` 변경시 필요없지만, $(사용자) ~ $ 이동시에는 PW가 필요하다.
        - 홈 디렉터리 생성여부에 따라 useradd / adduser로 구분된다.
        
        |구분|useradd|adduser|
        |---|---|----|
        |PW|별도 지정|생성시 지정|
        |home디렉토리|별도 지정|자동생성|
    
    - 계정확인:
        ```
        # cat /etc/passwd
        ```
        ```
        user:x:1000:1000::home/user:bin/sh
        mycha:x:1001:1001::home/mycha:bin/sh
        ```
        사용자이름:패스워드(사용x):UID:GID::사용자home:로그인쉘
    
    - 쉘 변경
        ```
        $ chsh --help
        $ chsh -s /bin/bash 
        ```

    4. 권한
        1. user1은 user2에 가서 생성 등을 할 수 없다.
            - 방법1. sudo 명령어 권한 부여
                ```
                # usermod aG sudo user1
                ```
                - user1에 sudo가 없으면 설치해야함: `apt-get install sudo`
                
                - user1으로 .home/user2 접근 -> sudo mkdir -> 소유권한은 root

            - 방법2. (보조그룹) user2의 가족이 된다.
                ```
                # usermode -aG user2 user1
                ```
                ```
                # cat etc/group 
            ```
        2. ls -al

            `d rwxr-xr-x 1 root root 4096 Feb 27 02:28 ..`\
            `- rw-r--r-- 1 user1 user1 220 Feb 27 02:28 .bash_logout`

            - 분해해보자
                1 영역: 파일의 종류 
                2 영역: 파일 권한 해당 필드의 사용자가 파일에 적용할 수 있는 권한
                    - rwx r-x r-x : 소유자 권한, 소유그룹 권한, 기타사용자 권한
                    - 권한표기종류 : r(read) w(writh) x(execute)
                3 영역: 링크 (바로가기가 몇개인지)
                4 영역: 소유자
                5 영역: 소유그룹
                6 영역: 파일크기 (byte)
                7 영역: 최종 수정시간
                8 영역: 이름  
        
            리눅스는 모든게 파일이다.
            계정정보, 패스워드, 그룹정보 모두 파일에 저장되어 있다.
            디렉터리도 파일이다?
            윈도우와의 차이는? = 확장자가 없다.
            숨겨진 파일은 `.`으로 시작된다.

            - `ls`: 파일을 정보를 확인
            - `cat` : 내용을 확인
                - head, tail
            - `vim`: 파일을 편집
        3. 권한 수정
            - user1, user2 생성, tmp에서 작업
            - user1으로 파일 생성 후 권환 확인

            |8진수|표시되는 퍼미션|의미|
            |---|---|---|
            |0|`---`| 접근이 불가능한 상태|
            |1|`--x`| 실행만 가능|
            |2|`-w-`| 쓰기만 가능|
            |3|`-wx`| 쓰기랑 실행 가능|
            |4|`r--`| 읽기만 가능함|
            |5|`r-x`| 읽기와 실행만 가능(프로그램)|
            |6|`rw-`| 읽기와 쓰기 가능(일반파일)|
            |7|`rwx`| 모든권한|

            - 파일권한 변경
                ```
                chmod mode <filename>
                ```
                - mode 값: 
                    - 심볼릭 모드 `who op permission` -> 예: `u+x g-r o-r`권한을 더하거나 빼기
                    - who: u: 소유자, g: 그룹, o: 기타사용자


            - 파일의 권환
                - 읽기 : cat, more, cp 등 파일을 내용을 읽어올 수 있음, 수정x, 복사o
                - 쓰기(수정) : echo, vim 등을 이용해 수정/변경할 수 있음, 덧붙임o, 삭제o, 읽기x
                - 실행 : shell 에서 실행 가능함
                    - 독립적인 사용이 불가능, 읽기+실행== 실행가능
            - 디렉토리의 권환
                - 읽기 : ls, dir등 내부의 내용(안의 파일목록?)을 읽음
                - 쓰기 : mkdir, touch, rm, rv로 생성/삭제/수정 가능
                - 실행 : =접근권환 `cd <dir>`

    7. 쳐보기
        1. 옵
            - `echo 'hello wold' > filetest1` -> echo출력될 문자가 filetest1으로 전달된다.
            - 2개는 아래(아랫줄?)에 추가된다.
            - cat filetest1 으로 잘 들어갓는지 확인이 가능하다.
        2. 옵2
            - Q: user1로 bashrc 파일에 alias myoh='touch "$(data)"' 추가
            ```
            $ bash
            $ cd ~
            $ myoh
            $ ls -al
            ```
            - A: cat으로 찾은다음엔 뭐해야하지 흠
            ```
            $ cat ~/.bachrc
            ```
            - vim으로 수정하고 :wd로 나와서 문제 명령어 수행하면 되는데 흠..
    
    8. docker img 
     저장해보고, 남의것 받아보기 

    9. docker로 streamlit 배포해보기 [공식](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)
        1. docker file 만들기
        2. 
            ```
            sudo docker build -t myoh0623/
            ```


*컨테이런란?
 - 실행을 위해 필요한 모든 요소를 포하함 소프트웨어 패키지
 - 운영체제를 가상화
 - 데이터센터, 클라우드, 노트북, 데스크 탑 어디에서나 실행이된다.
 예) 컴퓨터환경에서 개발된 코드를 내 노트북에서도 되게끔
 - 컨테이너 이전에는 Virtual Machine을 사용하고, 자원까지 가상화했다. 차이점을 보고싶다면 [참고](https://www.netapp.com/blog/containers-vs-vms/)

도커 이미지 전체 삭제
```
sudo docker images -a
sudo docker rmi -f $(sudo docker ps -a -q)
```

# Docker를 이용해서 Linux 익숙해지기
- docker를 이용해 ubuntu container를 다운로드

- nslookup 설치
- sudo apt-get install dnsutils
명령어나 개념을 추가로 정리할 필요가 있다.

- sudo -i 와 sudo -s의 차이는?

