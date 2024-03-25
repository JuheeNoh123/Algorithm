package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
//push X: 정수 X를 스택에 넣는 연산이다.
//pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
//size: 스택에 들어있는 정수의 개수를 출력한다.
//empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
//top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

public class n_10828 {

    static int[] A;
    static int size=0;// 배열 요소의 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //Scanner stdIn = new Scanner(System.in);
        StringTokenizer st;
        StringBuilder sb= new StringBuilder();
        int N= Integer.parseInt(br.readLine());
        A=new int[N];
        for(int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine(), " ");
            //rule = stdIn.next();
            switch (st.nextToken()){
                case "push":
                    push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    sb.append(pop()).append('\n');
                    break;
                case "size":
                    sb.append(size()).append('\n');
                    break;
                case "empty":
                    sb.append(empty()).append('\n');
                    break;
                case "top":
                    sb.append(top()).append('\n');
                    break;
            }

        }
        System.out.println(sb);


    }

    static void push(int x){
        A[size]=x;
        size++;
    }

    //pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    static int pop(){
        if(size>0)  {
            int res = A[size-1];
            size--;
            return res;
        }
        else return -1;
    }

    static int size(){
        return size;
    }

    //empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    static int empty(){
        int res;
        if(size<=0) res =1;
        else res =0;
        return res;
    }


    //top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    static int top(){
        if(size>0) return A[size-1];
        else return -1;
    }
}
