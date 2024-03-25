//정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

//명령은 총 다섯 가지이다.

//1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
//2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
//3: 스택에 들어있는 정수의 개수를 출력한다.
//4: 스택이 비어있으면 1, 아니면 0을 출력한다.
//5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

//입력
//첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
//둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.
//출력을 요구하는 명령은 하나 이상 주어진다.


package baekjoon;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class n_28278 {

    static ArrayList<Integer> stack = new ArrayList<>();
    //static int[] stack=new int[1000000];    //스택
    static int ptr=0;  //스택 포인터

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)) ;
        //Scanner stdIn = new Scanner(System.in);
        StringBuilder sb=new StringBuilder();
        int N = Integer.parseInt(bf.readLine());    //명령의 수
        StringTokenizer st;
        for(int i=0;i<N;i++){
            st = new StringTokenizer(bf.readLine()," ");
            switch (st.nextToken()){
                case "1":     //1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
                    int x = Integer.parseInt(st.nextToken());
                    push(x);
                    break;
                case "2":     //2 : 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
                    sb.append(pop()).append('\n');
                    break;
                case "3":     //3: 스택에 들어있는 정수의 개수를 출력한다.
                    sb.append(ptr).append('\n');
                    break;
                case "4":     //4: 스택이 비어있으면 1, 아니면 0을 출력한다.
                    if(ptr<=0) sb.append(1).append('\n');
                    else sb.append(0).append('\n');
                    break;
                case "5":     //5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
                    sb.append(peek()).append('\n');
                    break;
            }
            //System.out.println(ptr);

        }
        System.out.println(sb);

    }

    //1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
    public static void push(int x){
        ptr++;
        stack.add(x);
        //System.out.println(stack.get(ptr-1));
    }

    //2 : 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    public static int pop(){
        if(ptr<=0) return -1;
        else{
            return stack.remove(--ptr);
        }
    }


    //5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    public static int peek(){
        if(ptr<=0) return -1;
        else{
            return stack.get(ptr-1);
        }
    }
}
