package baekjoon;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

//도수 정렬
public class N_11931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] data = new int[n];

        for(int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }

        //최댓값 찾기
        int max = data[0];
        for(int i = 1; i < data.length; i++) {
            if(data[i] > max) {
                max = data[i];
            }
        }

        //최솟값
        int min = data[0];
        for(int i = 1; i < data.length; i++) {
            if(data[i] < min) {
                min = data[i];
            }
        }

        int[] cnt = new int[max + 1 - min];

        //System.out.println(cnt.length);

        for(int i = 0; i <n; i++) {
            if(data[i]<0) cnt[data[i]-min]++;
            else cnt[data[i]-min]++;
        }

//        for(int i = 0; i <cnt.length; i++) {
//            System.out.println(cnt[i]);
//        }


        for(int i = cnt.length-1; i >= 0; i--) {
            while(cnt[i] > 0) {
                bw.write(String.valueOf(i + min)+'\n');
                cnt[i]--;
            }
        }

        bw.flush();
        bw.close();
    }
}
