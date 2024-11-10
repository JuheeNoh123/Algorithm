import java.util.Scanner;

public class Main {
//    static  int max3(int a,int b,int c){
//        int max = a;
//        if (max < b)
//            max = b;
//
//        if (max < c)
//            max = c;
//
//        return max;
//    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int a= stdIn.nextInt();
        int b = stdIn.nextInt();
        //int res = max3(1,3,2);
        //System.out.println(res);
        System.out.println(a+b);
    }


}