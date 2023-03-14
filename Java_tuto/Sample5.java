import java.io. * ;

class Sample5 {
    public static void main(String[] args) throws IOException
    {
        System.out.println("키와 몸무개를 입력하세요");

        BufferedReader br = 
            new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();

        Float num1 = Float.parseFloat(str1);
        Float num2 = Float.parseFloat(str2);

        System.out.println(num1+"이고 " + num2 + "입니다.");
    }    
}
