// 4장 전체 //
public class Sample6 {
    public static void main(String[] args)
    {
        int a = 0;
        int b = 0;
        int c = 0;
        
        b = a++;
        c = ++a;

        System.out.println("b: "+b);
        System.out.println("c: "+c);
        System.out.println("b+c: "+b+c+'다');
        System.out.println("(b+c): "+(b+c)+'다');
    }   
}