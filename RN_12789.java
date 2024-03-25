package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class RN_12789 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<Integer> A = new LinkedList<>();  //기존 대기열
        Stack<Integer> X = new Stack<>();   //추가 대기열

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for (int i=0; i<N;i++){
            A.offer(Integer.parseInt(st.nextToken()));      //A에 데이터 인큐
        }

        int start = 1;

        while (!A.isEmpty()){
            if(A.peek()==start){
                A.poll();
                start++;
            }
            else if(!X.isEmpty() && X.peek()==start){    //추가 대기열이 비어있지 않고, 현재 번호표와 같다면 삭제
                X.pop();
                start++;
            }
            else{   //대기 순번이 아니면 추가 대기열로 이동
                X.push(A.poll());
            }
        }

        while(!X.isEmpty()){    //A(기존 대기열)가 비고 X(추가 대기열)가 비지 않았을때
            if(X.peek()==start){
                X.pop();
                start++;
            }
            else{
                System.out.println("Sad");
                return;
            }
        }

        System.out.println("Nice");
    }
}

