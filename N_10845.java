package baekjoon;
//push X: 정수 X를 큐에 넣는 연산이다.
//pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//size: 큐에 들어있는 정수의 개수를 출력한다.
//empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
//front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class N_10845 {
    static int size,back, front= 0;
    //size : 데이터 개수
    static int[] A;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());    //명령수
        A = new int[2000000];
        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine()," ");
            switch (st.nextToken()){
                case "push": //push X: 정수 X를 큐에 넣는 연산이다.
                    push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop": //pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                    sb.append(pop()).append("\n");
                    break;
                case "size": //size: 큐에 들어있는 정수의 개수를 출력한다.
                    sb.append(size).append("\n");
                    break;
                case "empty": //empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
                    if(size==0) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                case "front": //front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                    if(size!= 0) sb.append(A[front]).append("\n");
                    else sb.append(-1).append("\n");
                    break;
                case "back": //back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                    if(size!= 0) sb.append(A[back-1]).append("\n");
                    else sb.append(-1).append("\n");
                    break;
            }

        }

        System.out.print(sb);


    }

    public static int push(int data){//push X: 정수 X를 큐에 넣는 연산이다.
        if(size<2000000) {
            A[back++]=data;
            size++;
            if(back==2000000) back=0;
        }
        return 0;
    }
    public static int pop(){//pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if(size==0) return -1;
        int x = A[front++];
        size--;
        if(front==2000000) front = 0;

        return x;
    }


}
