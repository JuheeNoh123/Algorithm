package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class N_1158 {

    static Queue<Integer> q = new LinkedList<>();
    private static int front;  //맨 앞 인덱스
    private static int rear;   //맨 뒤 인덱스
    private static int capacity;   //큐 최대 용량
    private static int num;    // 현재 데이터 수



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) {
            q.offer(i);
        }

        sb.append("<");
        while(q.size() != 1) {
            // K - 1번째까지는 처음에 있던 값을 맨 뒤로 보낸다.
            for (int i = 0; i < S - 1; i++) {
                q.offer(q.poll());
            }
            // K번째 값은 poll한 후 출력한다.
            sb.append(q.poll() + ", ");
        }

        sb.append(q.poll()+">");

        System.out.println(sb);
    }


}
