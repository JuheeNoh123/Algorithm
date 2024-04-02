package baekjoon;

import java.io.*;
import java.util.StringTokenizer;

public class N_11399 {
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
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N= Integer.parseInt(bf.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(bf.readLine());

        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        heapSort(arr);

        int sum = 0;
        int sum2 = 0;

        for(int j=0;j<N;j++){
            //System.out.println("j : "+j);
            sum2 +=arr[j];
            //System.out.println("sum2 = " + sum2);
            sum += sum2;
            //System.out.println("sum = " + sum);
        }

        System.out.println(sum);

    }
}
