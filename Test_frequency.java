package baekjoon;
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
public class Test_frequency {
    static void heapSort(int[] arr) {
        int size = arr.length;
        for (int i = 1; i < size - 1; i++) {
            int c = i;
            while (c != 0) {
                int root = (c - 1) / 2;
                if (arr[c] > arr[root]) {
                    int temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }
                c = root;
            }
        }

        for (int i = size - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;
            int c = 1;
            int root = 0;

            do {
                c = root * 2 + 1;
                if (c < i - 1 && arr[c] < arr[c + 1]) {
                    c++;
                }

                if (c < i && arr[c] > arr[root]) {
                    temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }

                root = c;
            } while (c < i);
        }
    }



    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(bf.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }

        heapSort(arr);

        double sum = 0;
        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
            sum += arr[i];
        }
        double n = N;
        bw.write(Math.round(sum / n) + "\n");

        bw.write(arr[N / 2] + "\n");

        //bw.write(frequent(arr) + "\n");

        int range = arr[N - 1] - arr[0];
        bw.write(range + "\n");

        bw.flush();
        bw.close();
    }
}
