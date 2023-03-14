# 자바 기초하면서 애러 정리

### 컴파일시 한글이 깨지는 경우

- 작성한 코드
    ```java
    class Sample1
    {
        public static void main(String [] args)
        {
            System.out.println("JAVA start, 한글 되네?");
        }
    }
    ```
- 애러코드 : `error: unmappable character (0xEB) for encoding x-windows-949`
- 설명: vscode에서 run을 누르면 한글이 출력되지만, cmd에서 javac으로 컴파일 하면 애러가 발생한다.
- 원인: 설명에서 와 같이 encoding에서 깨짐으로 UTF8로 바꿔주면되지 않을까? 어? 그럼 vscode가 아닌 cmd에서는 어떻게 지정해주지? 했다. 
- 해결: `javac --help`가 역시 되더라. 컴파일에 encoding 옵션이 있는걸 확인 했다. `javac Sample1.java -encoding UTF8`으로 컴파일 해주면 끝.

