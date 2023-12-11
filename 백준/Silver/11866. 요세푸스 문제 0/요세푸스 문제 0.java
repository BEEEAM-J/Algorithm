import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int cnt = 1;

        Deque<Integer> josephus = new ArrayDeque<>();
        List<Integer> removedNum = new ArrayList<>();

        for(int i = 1; i <= N; i++) {
            josephus.add(i);
        }

        while(true) {
            if(josephus.size() > 1) {
                for(int i = 0; i < K - 1; i++) {
                    josephus.addLast(josephus.removeFirst());
                }
                removedNum.add(josephus.removeFirst());
            }
            else {
                removedNum.add(josephus.removeFirst());
                break;
            }
        }
        System.out.print("<");
        for(int n: removedNum) {
            if(cnt != N) {
                System.out.print(n + ", ");
            }
            else {
                System.out.print(n);
            }
            cnt ++;
        }
        System.out.print(">");
    }
}
