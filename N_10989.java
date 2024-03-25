package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class N_10989 {
    static void shellsort(int[] a, int n){
        int h;
        for (h=1;h<n;h=h*3+1)
            ;

        for(; h>0; h/=3){
            for(int i=h; i<n; i++){
                int j;
                int tmp = a[i];
                for(j=i-h; j>=0 && a[j]>tmp; j-=h){
                    a[j+h] = a[j];
                }
                a[j+h]=tmp;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] a= new int[n];
        for(int i=0;i<n;i++){
            a[i] = Integer.parseInt(br.readLine());
        }

        shellsort(a,n);

        for(int i =0;i<n;i++){
            sb.append(a[i]).append('\n');
        }

        System.out.println(sb);
    }
}
