class Car {
    private int num;
    private double gas;
    
    public Car(){
        num = 0000;
        gas = 0.1;
        System.out.println("신규 Car 생성");
    }

    public void setNumGas(int n, double g)
    {
        if (g>0 && g<1000){
            this.gas = g;
            this.num = n;
            this.show();
        }
        else{
            System.out.println("잘못된 값");
        }
    }

    void show()
    {
        System.out.println("번호: "+num);
        System.out.println("연료: "+gas);
    }

    void setNum(int n)
    {
        num = n;
        System.out.println("번호변경 :"+num);
    }

    void setGas(double g)
    {
        gas = g;
        System.out.println("가스변경 :"+gas);
    }
}

class SampleCar
{
    public static void main(String[] args)
    {
        Car car1;
        car1 = new Car();
        
        /* private로 필드변수를 변경해서 사용불가 
        car1.num = 1234;
        car1.gas = 20.5;
        car1.show();*/
      
        car1.setNum(3478);
        car1.setGas(15.3);
        car1.show();

        car1.setNumGas(1999, -11.97);
    }
}
