package baekjoon;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;

public class N_9012 {
    public static void main(String[] args) {
        int N;
        Scanner stdIn = new Scanner(System.in);
        N = stdIn.nextInt();
        String data;

        ArrayList<Character> A = new ArrayList<>();
        StringBuilder sb = new StringBuilder();


        for (int i =0;i<N;i++){
            data = stdIn.next();
            for(int j=0;j<data.length();j++){
                A.add(data.charAt(j));
            }
            //int S = A.size();
            //System.out.println(i+"번째------------------------------------------------");
            int k=1;
            while (true){
                if( A.size()!= 1){
                    if(k!= 0 && k<A.size()){
                        if(Objects.equals(A.get(k - 1),'(')) {
                            if (Objects.equals(A.get(k), ')')) {
                                //System.out.println("K : " + k);
                                //System.out.println(A);
                                A.remove(k);
                                A.remove(k - 1);
                                k = 0;
                                //System.out.println("K : " + k);
                                //System.out.println(A);
                            }
                        }
                    }
                }

                if(k<A.size()) {
                    k++;
                    //System.out.println("K : "+k);
                    //System.out.println("size : "+A.size());
                    //System.out.println(A);
                }

                else{
                    if(A.isEmpty()) {
                        sb.append("YES\n");
                        break;
                    }
                    else {
                        sb.append(("NO\n"));
                        break;
                    }
                }

            }
            A.clear();
            //System.out.println(A);

        }
        System.out.print(sb);
    }
}
