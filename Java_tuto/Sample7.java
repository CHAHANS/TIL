// 4장 마지막 형변환과 연산 //
class Sample7 {
     public static void main(String[] arg)
     {
        int a = 5;
        int b = 4;
        double c = a/b;
        double d = (double)a/(double)b;
        //int/int -> int로 반한되어 double c//
        System.out.println("int a/b(1)"+c);
        // int/int -> double 반한되어 double d//
        System.out.println("double a/b(2)"+d);
     }
    
}
