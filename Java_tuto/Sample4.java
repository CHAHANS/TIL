import java.io. * ;

class Sample4 {
    public static void main(String[] args) throws IOException
    {
        /* 문자열을 입력받을 수 있다. */
        System.out.println("문자열을 입력하세요");

        BufferedReader br = 
            new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        //입력된 문자열을 가리키는 변수 str 사용

        System.out.println(str + "가 입력되었습니다.");
        
        
        /* 정수를 받을 땐 변환해준다
        int num = Integer.parseInt(str);
        System.out.println(num + "으로 정수화 했습니다.");
        */
    }
    
    
}
