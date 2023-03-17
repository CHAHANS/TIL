// 인터페이스 그리고 멀티인터페이스를 해봄
interface iVehicle
{
    void vShow();
}
// 두번째 인터페이스
interface iMaterial
{
    void mShow();
}


// 인터페이스 사용예시
class iCar implements iVehicle, iMaterial
{
    private int num; private double gas;
    public iCar(int n, double g)
    {
        num = n; gas = g;
        System.out.println("번호: "+num+"그리고 가스: "+gas+"로 만들어졌다.");

    }
    public void vShow()
    {
        System.out.println("번호: "+num);
        System.out.println("가스: "+gas);
    }
    public void mShow()
    {
        System.out.println("원료는 철이다.");
    }
}

class iPlane implements iVehicle
{
    private int flight;

    public iPlane(int f)
    {
        flight = f;
        System.out.println("만들어진 iPlane의 번호: "+flight);
    }

    public void vShow()
    {
        System.out.println("번호: "+flight);
    }
}

class SampleI1
{
    public static void main(String[] args)
    {
        iVehicle[] ivc;
        ivc = new iVehicle[2];

        ivc[0] = new iCar(1234, 20.1);
        ivc[1] = new iPlane(5678);

        for(int i=0; i<ivc.length; i++){
            ivc[i].vShow();
        }
    }
}

class SampleI2
{
    public static void main(String[] args)
    {
        iCar car1 = new iCar(1324, 11.5); 
        car1.vShow();
        car1.mShow();
    }
}