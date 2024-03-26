package baekjoon;


import java.util.Scanner;

public class N_2751_merge {
    public static  int[] tempArr;

    public static void main(String[] args) {
        int n;
        Scanner std = new Scanner(System.in);
        n = std.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++){
            arr[i] = std.nextInt();

        }

        mergeSort(arr, 0, arr.length-1);

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
    public static void mergeSort(int arr[], int start, int end){

        if(start<end){
            int mid = start+((end-start)/2);
            mergeSort(arr, start, mid);
            mergeSort(arr, mid+1, end);
            merge(arr, start, mid, end);
        }
    }

    public static void merge(int arr[], int start, int mid, int end) {
        int leftIdx = start; // 왼쪽 부분 배열의 시작 인덱스
        int rightIdx = mid + 1; // 오른쪽 부분 배열의 시작 인덱스
        int tempIdx = 0; // 임시 배열의 인덱스

        while (leftIdx <= mid && rightIdx <= end) {
            if (arr[leftIdx] <= arr[rightIdx]) {
                tempArr[tempIdx++] = arr[leftIdx++];
            } else {
                tempArr[tempIdx++] = arr[rightIdx++];
            }
        }

        while (leftIdx <= mid) {
            tempArr[tempIdx++] = arr[leftIdx++];
        }

        while (rightIdx <= end) {
            tempArr[tempIdx++] = arr[rightIdx++];
        }

        for (int i = start; i <= end; i++) {
            arr[i] = tempArr[i];
        }
    }
}
