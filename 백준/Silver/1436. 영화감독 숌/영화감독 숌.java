import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        int compare = 665;

        while(true) {
            if(String.valueOf(compare).contains("666")) {       // 숫자에 666 있는지 확인
                cnt ++;
            }

            if(cnt == N) {
                System.out.println(compare);
                break;
            }

            compare ++;
        }

    }
}