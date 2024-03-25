package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class n_1920 {
//    static void swap(int[] a,int idx1, int idx2){
//        int t = a[idx1];
//        a[idx1] = a[idx2];
//        a[idx2] = t;
//        //7,8 -> a[8] , a[7]
////        for(int i=0;i<5;i++){
////            System.out.print(a[i]);
////        }
////        System.out.println("");
//    }
//
//    static void bubble(int[] A, int n){
//        for(int i=0;i<n-1;i++){
//            for(int j=n-1;j>i;j--){
//                if(A[j-1]>A[j]) swap(A,j-1,j);  //j가 바뀌어야 할 때마다 호출
//            }
//            //System.out.print(A[i]);
//
//        }
//        //System.out.println("");
//    }
//    static int binSearch(int arrM, int[] A, int n){
//        int pl = 0;
//        int pr = n-1;
//        int res = 0;
//        for(int i=0;i<n;i++){   //A배열 순환
//            do{ //이진 탐색
//                int pc = (pl+pr)/2;
//                if(A[pc]==arrM) {
//                    res=1;
//                    break;
//                }
//                else if(A[pc] > arrM) pr=pc-1;
//                else pl=pc+1;
//            }while(pl<=pr);
//        }
//        //System.out.println(res);
//        return res;
//    }
    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        //배열 요소 수 입력
        int n= stdIn.nextInt();
        //배열 값 입력
        int[] A = new int[n];
        for (int i=0;i<n;i++){
            A[i] = stdIn.nextInt();
        }

        //bubble(A,n);
//        for(int i=0;i<n;i++){
//            System.out.print(A[i]); //A={1,2,3,4,5}
//        }
        Arrays.sort(A);

        System.out.println("오름차순 정렬 완료");


        //검색할 요소 수 입력
        int M = stdIn.nextInt();
        //검색할 배열 값 입력
        int[] arrM = new int[M];

        //출력할 값 저장할 배열
        int[] res = new int[M];

        for(int i=0;i<M;i++){
            arrM[i] = stdIn.nextInt();
            int in = Arrays.binarySearch(A,arrM[i]);
            if(in<0) res[i] = 0;
            else res[i] =1;
            System.out.println(res[i]);

        }


    }
}
