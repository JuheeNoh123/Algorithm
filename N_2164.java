package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class N_2164 {
    private static int[] que;
    private static int front;  //맨 앞 인덱스
    private static int rear;   //맨 뒤 인덱스
    private static int capacity;   //큐 최대 용량
    private static int num;    // 현재 데이터 수
    //큐 생성
    public static void IntQueue(int maxlen){
        front=0;
        rear=0;
        num=0;
        capacity=maxlen;
        que=new int[capacity];
        for(int i=0;i<capacity;i++){
            enque(i+1);
        }
    }

    //뒤에 추가(인큐)
    public static void enque(int x){
        que[rear++]=x;
        num++;
        if(rear==capacity) rear=0;
        //System.out.println("num:"+num);
        //System.out.println("rear:"+rear);
    }

    //앞에서 빼기(디큐)
    public static int deque(){
        int x = que[front++];
        num--;
        if(front==capacity) front=0;
        //System.out.println("num:"+num);
        //System.out.println("front:"+front);
        return x;
    }

    //큐 안의 데이터 출력
    public static void dump(){
        //if(num<=0) System.out.println("큐가 비어있다");
        for(int i=0;i<num;i++){
            System.out.print(que[(i+front)%capacity]+ " ");
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N= Integer.parseInt(br.readLine());
        IntQueue(N);
        int i=0;
        //System.out.println("------------------");
        while(num!=1){
            //System.out.println(i+"단계");
            int deq = deque();
            if(i%2==1) enque(deq);
            //dump();
            i++;
        }
        dump();
    }
}
