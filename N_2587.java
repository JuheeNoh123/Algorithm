package baekjoon;

import java.util.Scanner;

public class N_2587 {
    static void heapSort(int[] arr){
        //완전 이진트리 만들기(상향식)
        int size = arr.length;
        for(int i=1;i<size;i++){
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


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        int sum =0;
        for(int i=0;i<5;i++){
            arr[i] = sc.nextInt();
            sum += arr[i];
        }
        heapSort(arr);

        System.out.println(sum/5);
        System.out.println(arr[2]);
    }
}
