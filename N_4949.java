package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class N_4949 {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st;


        while(true){
            st = br.readLine();
            if(st.equals(".")) break;
            sb.append(solve(st)).append('\n');
        }

        System.out.println(sb);
    }

    public static String solve(String st){
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<st.length();i++){
            char a = st.charAt(i);
            if(a=='('||a=='[') stack.push(a);
            else if(a==')') {
                if(stack.empty()|| stack.peek() !='(' ){
                    return "no";
                }

                else stack.pop();
            }

            else if(a==']'){
                if(stack.empty() || stack.peek() != '[') {
                    return "no";
                }
                else stack.pop();
            }

        }
        if(stack.empty()) return "yes";
        else return "no";

    }
}
