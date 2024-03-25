package baekjoon;

import java.io.*;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;

public class N_1427 {

    static void quickSort(ArrayList<Integer>  a, int left, int right){
        Stack<Integer> lstack = new Stack<Integer>();  //right-left+1 : 나눌 배열의 요소 수
        Stack<Integer> rstack = new Stack<Integer>();


        lstack.push(left);
        rstack.push(right);

        while (!lstack.isEmpty()) {
            int pl = left = lstack.pop();     //왼쪽 커서
            int pr = right = rstack.pop();    //오른쪽 커서
            int x = a.get((left + right) / 2);        //피벗(가운데 요소)

            do {
                while (a.get(pl) < x) pl++;
                while (a.get(pr) > x) pr--;
                if (pl <= pr) Collections.swap(a, pl++, pr--);
            } while (pl <= pr);

            //요소의 개수가 두개 이상일 때
            if(left<pr){
                lstack.push(left);
                rstack.push(pr);
            }
            if(pl<right){
                lstack.push(pl);
                rstack.push(right);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> a = new ArrayList<>();

        BigInteger num = new BigInteger(br.readLine());
        String numStr = num.toString();
        for (int i = 0; i < numStr.length(); i++) {
            int digit  = numStr.charAt(i) - '0';
            a.add(digit);
        }

        quickSort(a, 0,  a.size() - 1);
        for(int i=a.size()-1;i>=0;i--){
            bw.write(a.get(i)+"");
        }
        bw.flush();
        bw.close();
    }
}
