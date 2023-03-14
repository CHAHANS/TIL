import java.io.*;

class Sample8 {
    public static void main(String[] args) throws IOException
    {
        System.out.println("응시자 수를 입력하세요");
        BufferedReader br = 
            new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int num = Integer.parseInt(str);

        int[] test = new int[num];
        
        System.out.println("응시자 수 만큼 점수 입력");
        
        for(int i=0; i<num; i++){
            str = br.readLine();
            int tmp = Integer.parseInt(str);
            test[i] = tmp;
        }

        for(int i=0; i<num; i++){
            System.out.println((i+1)+"번째 점수는 "+test[i]+"입니다.");
        }
    }
    
}
