package baekjoon;

import java.util.Scanner;

public class N_2839 {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int cnt =0;
        int a = stdin.nextInt();
        while (a>=0){
            if(a%5==0) {
                cnt = a/5;
                break;
            }
            else{
                a=a-3;
                cnt++;
                if(a%5==0){
                    cnt = cnt+ a/5;
                    break;
                }
            }


        }
        if(a<0) cnt = -1;
        System.out.println(cnt);
    }
}
