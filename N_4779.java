package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_4779 {
    static int n;
    static StringBuilder answer;


    public static void del(int start, int size){
        if (size ==1) return;
        int newsize = size/3;


        for(int i=start+newsize; i<start+newsize*2;i++){
            answer.setCharAt(i,' ');
        }

        del(start, newsize);
        del(start+2*newsize, newsize);

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        while ((str = br.readLine()) != null) {
            n = Integer.parseInt(str);
            answer =new StringBuilder();
            int len = (int) Math.pow(3, n);
            for (int i = 0; i < len; i++) {
                answer.append("-");
            }

            del(0, len); // 시작 인덱스, 시작 길이
            System.out.println(answer);

        }
    }


}
