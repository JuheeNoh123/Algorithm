package baekjoon;

import java.io.*;
import java.util.StringTokenizer;

//도수 정렬
public class N_10817 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] data = new int[3];
        for(int i = 0; i < 3; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        int max = data[0];
        for(int i = 1; i < 3; i++) {
            if(data[i] > max) {
                max = data[i];
            }
        }

        int[] cnt = new int[max+1];
        for(int i = 0; i < 3; i++) {
            cnt[data[i]]++;
        }

        int[] ans = new int[3];
        int ans_idx = 0;
        for(int i = 0; i < cnt.length; i++) {
            while(cnt[i] > 0) {

                //bw.write(String.valueOf(i)+'\n');
                ans[ans_idx++] = i;
                cnt[i]--;
            }
        }

        bw.write(String.valueOf(ans[1]));


        bw.flush();
        bw.close();
    }
}
