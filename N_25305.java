package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class N_25305 {
    static void swap(int[] a, int idx1, int idx2){
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void quicksort(int[] a, int left, int right){
        int pl = left;
        int pr = right;
        int m = a[(pl+pr)/2];

        do{
            while(a[pl] < m) pl++;
            while(a[pr] > m) pr--;
            if(pl<=pr) swap(a, pl++, pr--);
        }while(pl<=pr);

        if(left<pr) quicksort(a, left, pr);
        if(pl<right) quicksort(a, pl, right);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] a = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        quicksort(a,0,n-1);


        System.out.println(a[n-k]);

    }
}
