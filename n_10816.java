package baekjoon;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class n_10816 {


    static int lower(int[] arr, int key){
        int start = 0;
        int end = arr.length;
        int mid;
        while(start<end){
            mid = (start+end)/2;
            if(arr[mid]>=key) end = mid;
            else start = mid+1;
        }
        return end;
    }
    static int upper(int[] arr, int key){
        int start = 0;
        int end = arr.length;
        int mid;
        while(start<end){
            mid = (start+end)/2;
            if(arr[mid]>key) end = mid;
            else start = mid+1;
        }
        return end;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)) ;

        int N = Integer.parseInt(bf.readLine()); //숫자 카드 개수
        int[] arr = new int[N]; // 숫자 카드 배열

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i =0; i< N;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int M = Integer.parseInt(bf.readLine());    //찾을 수 개수
        st = new StringTokenizer(bf.readLine());// 배열 입력
        int[] find = new int[M];    //찾을 수 배열

        for(int i =0; i< M;i++){
            find[i] = Integer.parseInt(st.nextToken()); //배열 호출
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0;i<M;i++){
            int first = lower(arr, find[i]);
            int last = upper(arr,find[i]);

            sb.append(last - first).append(" ");
        }
        System.out.print(sb);







    }


}