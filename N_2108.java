package baekjoon;
import java.io.*;
/*
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
 */
public class N_2108 {
    static void heapSort(int[] arr){
        //완전 이진트리 만들기(상향식)
        int size = arr.length;
        for(int i=1;i<size;i++){
            int c = i;
            while (c!=0){
                int root = (c-1)/2;
                if(arr[c]>arr[root]){
                    int temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }
                c=root;

            }
        }


        //정렬하기
        for(int i=size-1;i>=0;i--){
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;
            int c = 1;
            int root = 0;

            do{
                c=root*2+1;
                if(c<i-1 && arr[c]<arr[c+1]){
                    c++;
                }

                if(c<i && arr[c]>arr[root]){
                    temp = arr[c];
                    arr[c] = arr[root];
                    arr[root] = temp;
                }
                root = c;
            }while(c<i);
        }
    }

    //최빈값
    static int frequent(int[] arr) {
        int count = 0;
        int max = -1;
        int cur_val = arr[0];
        boolean check = false;

        for(int i = 0;i< arr.length-1;i++){
            System.out.println("====================");
            System.out.println("i = "+i);
            if(arr[i]==arr[i+1]){
                count++;
                System.out.println("arr[i]==arr[i+1] : count "+count);
            }else{
                count = 0;
                System.out.println("arr[i]!=arr[i+1] : count "+count);
            }

            if (count > max) {
                max = count;
                cur_val = arr[i];
                check = true;
                System.out.println("if (count > max) : max=count , max "+max);
                System.out.println("if (count > max) : cur_val "+cur_val);
                System.out.println("if (count > max) : check "+check);
            }else if(max==count && check){
                cur_val = arr[i];
                check= false;
                System.out.println("else if(max==count && check) : cur_val "+cur_val);
                System.out.println("else if(max==count && check) : check "+check);
            }
            System.out.println("====================");

        }
        System.out.println("cur_val :"+ cur_val);
        return cur_val;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N= Integer.parseInt(bf.readLine());
        int[] arr = new int[N];
        double sum = 0;
        for(int i=0;i<N;i++){
            arr[i] = Integer.parseInt(bf.readLine());
            sum += arr[i];
        }

        heapSort(arr);


        bw.write(Math.round(sum/N)+"\n");
        bw.write(arr[(N-1)/2]+"\n");
        bw.write(frequent(arr)+"\n");
        bw.write((arr[N-1] - arr[0])+"\n");

        bw.flush();
        bw.close();
    }
}
