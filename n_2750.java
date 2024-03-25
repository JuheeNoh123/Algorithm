package baekjoon;

import java.util.Scanner;

//N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
public class n_2750 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        //배열 요소 수 입력
        int n= stdIn.nextInt();
        //배열 값 입력
        int[] A = new int[n];
        for (int i=0;i<n;i++){
            A[i] = stdIn.nextInt();
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                if(A[j]>A[j+1]) swap(j,j+1,A);
            }
        }

        for (int i=0;i<n;i++){
            System.out.println(A[i]);
        }

    }
    static void swap(int a, int b,int[] A){
        int c=A[a];
        A[a]= A[b];
        A[b]=c;
    }

}
