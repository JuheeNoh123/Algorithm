package baekjoon;

import java.util.Scanner;

public class shellSort2 {
    static void shellSort(int[] a, int n){
        int h;
        for (h=1;h<n;h=h*3+1)   // 초기 간격 h를 결정 : n/3 + 1
            ;   // 반복문의 바디가 비어 있으므로, 반복문은 초기화식을 실행하고, 조건식을 검사한 후에 바로 반복문을 종료
                // 반복문을 사용하는 목적 : 단순히 h 값 설정

        for(;h>0;h/=3)
            for(int i = h;i<n;i++){     //초기값 : 이전 반복문에서 설정한 'h'값
                int j;
                int tmp = a[i];
                for(j=i-h;j>=0 && a[j]>tmp;j -=h)
                    a[j+h]=a[j];
                a[j+h] = tmp;
            }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("셸 정렬");
        System.out.print("요소 수 : ");
        int n = stdIn.nextInt();
        int[] x = new int[n];

        for(int i=0;i<n;i++){
            System.out.print("x["+i+"] : ");
            x[i] = stdIn.nextInt();
        }

        shellSort(x,n);

        System.out.println("오름차순으로 정렬 완료");
        for(int i=0;i<n;i++){
            System.out.println("x["+i+"] = "+ x[i]);
        }
    }
}
