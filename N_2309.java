package baekjoon;

import java.io.*;
import java.util.Arrays;

public class N_2309 {
    public static int[] ans = new int[9];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] data = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            data[i] = Integer.parseInt(br.readLine());
            sum += data[i];
        }

        sort(data);
        for (int i = 0; i < 9; i++) {
            for (int j = i + 1; j < 9; j++) {
                if(sum - data[i] - data[j]==100){
                    data[i] = 0;
                    data[j] = 0;

                }
            }
        }

        for (int i = 0; i < 9; i++) {
            System.out.println(ans[i]);
        }
    }

    public static void sort(int[] data) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int max = 0;
        for (int i = 0; i < 9; i++) {
            if (data[i] > max) {
                max = data[i];
            }
        }

        int[] cnt = new int[max + 1];

        for (int i = 0; i < 9; i++) {
            cnt[data[i]]++;
        }


        int index = 0;
        for (int i = 0; i < cnt.length; i++) {
            while (cnt[i] > 0) {
                ans[index] = i;
                index++;
                cnt[i]--;
            }
        }

        bw.flush();
        bw.close();
    }
}
