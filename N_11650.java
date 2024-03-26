package baekjoon;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class N_11650 {

    static int[][] temp;

    public static void mergeSort(int[][] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
    }

    public static void merge(int[][] arr, int start, int mid, int end) {
        int leftIdx  = start;
        int rightIdx = mid + 1;
        int k = start;

        while (leftIdx  <= mid && rightIdx <= end) {
            if (arr[leftIdx][0] < arr[rightIdx][0] || (arr[leftIdx][0] == arr[rightIdx][0] && arr[leftIdx][1] < arr[rightIdx][1])) {
                temp[k++] = arr[leftIdx++];
            } else {
                temp[k++] = arr[rightIdx++];
            }
        }

        while (leftIdx <= mid) {
            temp[k++] = arr[leftIdx++];
        }

        while (rightIdx <= end) {
            temp[k++] = arr[rightIdx++];
        }

        for (int index = start; index <= end; index++) {
            arr[index] = temp[index];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        temp = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        mergeSort(arr, 0, n - 1);

        for (int i = 0; i < n; i++) {
            bw.write(arr[i][0] + " " + arr[i][1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
