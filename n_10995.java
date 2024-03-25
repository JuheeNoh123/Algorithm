package baekjoon;

import java.util.Scanner;

public class n_10995 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = stdIn.nextInt();

        for(int i =0;i<N;i++){
            if(i%2==0){
                for(int j=0;j<N*2;j++){
                    if(j%2==0)sb.append("*");
                    else sb.append(" ");
                }
            }
            else{
                for(int j=0;j<N*2;j++){
                    if(j%2==1)sb.append("*");
                    else sb.append(" ");
                }
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
