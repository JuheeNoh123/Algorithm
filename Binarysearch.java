package baekjoon;

import java.util.Scanner;

public class Binarysearch {

    static  int binSearch(int[] x, int key, int num){
        int pl=0;
        int pr=num-1;
        int pc;
        do{
            pc = (pl+pr)/2;
            if(x[pc]==key) return pc;
            else if(x[pc]>key) pr=pc-1;
            else pl=pc+1;
        } while(pl<=pr);

        return -1;  //검색 실패!
    }
    public static void main(String[] args){
        Scanner stdIn = new Scanner(System.in);

        System.out.print("요소 수 : ");
        int num = stdIn.nextInt();
        int[] x = new int[num];

        System.out.println("오름차순으로 입력해주세요");
        System.out.print("x[0] : ");
        x[0] = stdIn.nextInt();
        for (int i = 1; i<num;i++){
            do{
                System.out.print("x["+i+"] : ");
                x[i] = stdIn.nextInt();
            }while(x[i-1]>x[i]); //바로 앞의 요소보다 작으면 다시 입력
        }

        System.out.print("검색할 값 : ");
        int key = stdIn.nextInt();

        int idx = binSearch(x,key,num);
        if(idx==-1) System.out.println("검색 실패");
        else System.out.println("검색하신 값은 x["+idx+"]에 있습니다.");

    }
}
