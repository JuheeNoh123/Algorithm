package baekjoon;

import java.util.Scanner;

public class N_11651 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        //y축
        int max = 0;
        for (int i = 0; i < n; i++) {
            if(arr[i][1] > max) {
                max = arr[i][1];
            }
        }

        int min = 0;
        for (int i = 0; i < n; i++) {
            if(arr[i][1] < min) {
                min = arr[i][1];
            }
        }

        //x축
        int max_x = 0;
        for (int i = 0; i < n; i++) {
            if(arr[i][0] > max_x) {
                max_x = arr[i][0];
            }
        }

        int min_x = 0;
        for (int i = 0; i < n; i++) {
            if(arr[i][0] < min) {
                min_x = arr[i][0];
            }
        }

        int[] cnt_y = new int[max-min+1];
        for (int i = 0; i < n; i++) {
            cnt_y[arr[i][1]-min]++;
        }

        int[] cnt_x = new int[max-min+1];
        for (int i = 0; i < n; i++) {
            cnt_x[arr[i][1]-min]++;
        }


        int index = 0;
        for(int i = 0; i < cnt_y.length; i++) {
            while(cnt_y[i] > 0) {
                
                arr[index][1] = i;
                index++;
                System.out.println();
            }
        }
    }
}
