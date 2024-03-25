package baekjoon;

import java.util.ArrayList;
import java.util.Scanner;

public class n_12789 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int N = stdIn.nextInt();
        int j = 1;
        //int k=0;
        ArrayList<Integer> A = new ArrayList<>();
        ArrayList<Integer> X = new ArrayList<>();


        for (int i = 0; i < N; i++) {
            int data = stdIn.nextInt();
            A.add(data);
            //A[ptr++]=A[i];
        }
        System.out.println("처음 A :" + A);
        //for(int i=0;i<N;i++){
        while (!A.isEmpty()) {
            //대기열을 1부터 N까지 정렬이 가능한지 확인 필요
            //1(j)이 아니면 X로 보내기
            //1(j)이면 없애기
            if (A.get(0) == j) {

                A.remove(0);
                j++;

            } else {
                X.add(A.get(0));
                A.remove(0);
            }

            System.out.println("j : " + j);
            System.out.println("A : " + A);
            System.out.println("X : " + X);
            System.out.println(" ");

            if (A.isEmpty() && X.isEmpty()) System.out.println("Nice");
        }

        System.out.println("-------------X 확인 -------------------");


        while (!X.isEmpty()) {
            int h = X.size() - 1;
            if (X.get(h) == j) {
                X.remove(h);

                if (X.isEmpty()) {
                    System.out.println("Nice");
                    break;
                } else {
                    j++;
                }
                System.out.println("j : " + j);
                System.out.println("A : " + A);
                System.out.println("X : " + X);
                System.out.println(" ");
            } else {
                System.out.println("j : " + j);
                System.out.println("A : " + A);
                System.out.println("X : " + X);
                System.out.println(" ");
                System.out.println("Sad");
                break;
            }

        }

    }

}

