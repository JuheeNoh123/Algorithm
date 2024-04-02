package baekjoon;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
 */
public class N_2108 {
    static void heapSort(int[] arr){
        //완전 이진트리 만들기(상향식)
        int size = arr.length;
        for(int i=1;i<size-1;i++){
            int c = i;
            while (c!=0){
                int root = (c-1)/2;
                if(arr[c]>arr[root]){
                    int temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }
                c=root;
            }

        }

        //정렬하기
        for(int i=size-1;i>=0;i--){
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;
            int c = 1;
            int root = 0;

            do{
                c=root*2+1;
                if(c<i-1 && arr[c]<arr[c+1]){
                    c++;
                }

                if(c<i && arr[c]>arr[root]){
                    temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }
                root = c;
            }while(c<i);
        }
    }

    //최빈값
    static int frequent(int[] arr) {
        int c = 1;
        int max = 0;
        int value = arr[0];

        for(int i = 1;i< arr.length-1;i++){
            if(arr[i]==arr[i-1]){
                c++;
            }else{
                if(c>max){
                    max = c;
                    value = arr[i-1];
                }
                c=1;
            }
        }

        //배열 마지막 요소 처리
        if(c>max){
            max = c;
            value = arr[arr.length-1];
        }

        if(max ==1){
            //value = arr[1];
        }

        return value;
    }








    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N= Integer.parseInt(bf.readLine());
        int[] arr = new int[N];
        int cnt = 0;
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(bf.readLine());

        }

        heapSort(arr);

        //평균 출력
        double sum = 0;
        for(int i=0;i<N;i++){
            System.out.println(arr[i]);
            sum += arr[i];
        }
        double n = N;
        bw.write("평균"+Math.round(sum/n)+"\n");
        bw.write("중앙값"+arr[N/2]+"\n");
        bw.write("최빈값"+frequent(arr)+"\n");
        int range = arr[N-1] - arr[0];
        bw.write("차이"+range+"\n");
        bw.flush();
        bw.close();
    }
}
