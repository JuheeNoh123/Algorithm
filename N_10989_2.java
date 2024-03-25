package baekjoon;

import java.io.*;

public class N_10989_2 {

    static void swap(int[] a, int idx1, int idx2){
        int t = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = t;
    }

    static void quickSort(int[] a, int left, int right){
        int pl = left;
        int pr = right;
        int m =  a[(pl + pr) / 2];

        do{
            while(a[pl]<m) pl++;
            while(a[pr]>m) pr--;
            if(pl<=pr) swap(a,pl++,pr--);
        }while(pl<=pr);

        if(left<pr) quickSort(a,left,pr);
        if(pl<right) quickSort(a,pl, right);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        for(int i=0;i<n;i++){
            a[i] = Integer.parseInt(br.readLine());
        }
        quickSort(a, 0, n-1);
        for(int i=0;i<n;i++){
            bw.write(a[i]+"\n");
        }
        bw.flush();
        bw.close();
    }
}
