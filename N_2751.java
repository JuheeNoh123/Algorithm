
package baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class N_2751 {
    //N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = sc.nextInt();

        ArrayList<Integer> list = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            list.add(sc.nextInt());
        }

        Collections.sort(list);

        for(Integer c : list) {
            sb.append(c).append("\n");
        }

        System.out.println(sb);
    }




}
