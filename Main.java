package baekjoon;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;  //요소 수
        n = stdIn.nextInt();

        int[] arr = new int[n+1];     //배열 선언
        for (int i=0;i<n;i++){
            arr[i] = stdIn.nextInt();   //배열 입력
        }

        int M = stdIn.nextInt();
        int[] keys = new int[M];
        for (int i=0;i<M;i++){
            keys[i]=stdIn.nextInt();    //M개의 수 입력
        }
        
        for (int i=0;i<M;i++){ //보초법 사용
            arr[n]=keys[i]; //보초 추가
            int res = search(arr,keys[i],n);
            System.out.println(res);
        }

    }

    static int search(int[] arr, int key, int n){
        int i = 0;
        while (key != arr[i]) {
            i++;
        }
        return i==n ? 0:1;
    }
}