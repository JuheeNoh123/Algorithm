package baekjoon;

import java.util.Scanner;

public class Shellsort {
    static void shellSort(int[] a, int n){
        for(int h=n/2; h>0;h/=2){   //시작 위치가 중간, 0이 될 때까지, h는 반씩 줄어듦
            System.out.print("{");
            for(int k=0;k<n;k++) System.out.print(a[k]+",");
            System.out.println("}");

            for(int i=h;i<n;i++){
                int check = 0;
                int j;
                int tmp = a[i];
                System.out.println("==========================");
                System.out.println("(구간)h : "+ h);
                System.out.print ("비교  tmp(a["+i+"]) : "+ tmp+"  |   ");

                //비교 & 대입
                for(j=i-h; j>=0 && a[j]>tmp;j-=h){  //j가 0보다 커야하고, 비교할값보다 커야함
                    check = 1;
                    a[j+h] = a[j]; // 삽입
                    System.out.println("a["+j+"] : "+a[j]);
                    System.out.print("{");
                    for(int k=0;k<n;k++) {
                        System.out.print(a[k]+",");
                    }
                    System.out.println("}");
                }
                if(check==0) System.out.println("a["+j+"] : "+a[j]+" [X(이미 작음)]");
                a[j+h] = tmp;
                System.out.print("{");
                for(int k=0;k<n;k++) System.out.print(a[k]+",");
                System.out.println("}");

                System.out.println();
            }
            System.out.println("===============비교 끝================");
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
