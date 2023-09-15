abstract class Vehicle 
{
    protected int speed;
    
    public void setSpeed(int s)
    {
        speed = s;
        System.out.println("속도를" + speed +"로 변경했음");
    }
    abstract void show();
}

//추상 클레스 확장해보기
class Motorcycle extends Vehicle
{
    private int num;
    private double gas;

    public Motorcycle(int n, double s)
    {
        num=n;
        gas=s;
        System.out.println("오토바이생성 완료. 번호: " + num + " 가스: " + gas);
    }

    public void show()
    {
        System.out.println("번호: " + num);
        System.out.println("가스: " + gas);
        System.out.println("속도: " + speed);
    }
}

class Plane extends Vehicle
{
    private int flight;

    public Plane(int f)
    {
        flight = f;
        System.out.println("비행기 완료. 번호: " + flight);
    }

    public void show()
    {
        System.out.println("번호: " + flight);
        System.out.println("속도: " + speed);
    }
}

class SampleAb
{
    public static void main(String[] args)
    {
        
        Vehicle[] vc;
        vc = new Vehicle[2];

        vc[0] = new Motorcycle(1234, 20.5);
        vc[0].setSpeed(60);
        vc[1] = new Plane(5678);
        vc[1].setSpeed(200);

        for(int i = 0; i<vc.length; i++) {
            vc[i].show();
        }

    }
}

class SampleAb2
{
    public static void main(String[] args)
    {
        Vehicle[] vc;
        vc = new Vehicle[2];

        vc[0] = new Motorcycle(1234, 20.5);
        vc[0].setSpeed(60);
        vc[1] = new Plane(5678);
        vc[1].setSpeed(200);

        for(int i = 0; i<vc.length; i++) {
            if(vc[i] instanceof Motorcycle)
                System.out.println((i+1)+"번째는 오토바이다.");
            else if(vc[i] instanceof Plane)
                System.out.println((i+1)+"번째는 비행기다.");
        }
    }
}