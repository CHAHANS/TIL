# 기본셋팅에 생성된 애러

1. python3의 기본버전이 3.6이라 3.8을 설치하고, 버전을 변경하기 위해 아래작업을 수행
    1. 설치된 버전 확인
    ```
    ls -al /usr/bin/python*
    ```
    2. python3.8이 없다면 설치
    ```
    $ sudo apt-get install python3.8
    ```

    3. update-alternatives 패키지를 설치
    ```
    $ sudo apt-get install update-alternatives
    ```

    4. 경로에 python3.8을 추가하고 우선순위를 1위로 변경
    ```
    $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
    ```
    - 마지막에 1이 우선순위를 나타낸다. --install 옵션을 사용할 때 필요한 인자를 잘 확인하자. 오타자 자주난 부분이다.

2. python 경로를 바 꾼 후에 pip가 인식되지 않음
    - 애러 : `ModuleNotFoundError: No module named 'pip._internal'`
    - pip를 재설치 해도 되지 않음
    - 경로 문제인가 고민하다가 업데이트로 해결될까 ?라는 의문
    - pip를 업그레드 해서 해결함, pip와 pip3 같은 문제 같은 방법으로 해결됨
    ```
    python -m pip install --upgrade pip
    ```

3. venv 
